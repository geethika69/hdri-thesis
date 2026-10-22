"""Build a directed, weighted service dependency graph from trace spans.

Input: iterable of span dicts with keys
  trace_id, span_id, parent_span_id (None for roots), service.
Edge direction: caller -> callee (call direction), as fixed in Chapter 1.
Edge weight: number of observed calls. An edge is created when a span's parent
belongs to a different service. Asynchronous links through queues are NOT
visible here (known limitation).
"""
from collections import Counter
import networkx as nx


def build_graph(spans):
    spans = list(spans)
    by_id = {(s["trace_id"], s["span_id"]): s for s in spans}
    calls = Counter()
    services = set()
    for s in spans:
        services.add(s["service"])
        pid = s.get("parent_span_id")
        if pid is None:
            continue
        parent = by_id.get((s["trace_id"], pid))
        if parent is None:
            continue  # orphan span: parent not collected
        if parent["service"] != s["service"]:
            calls[(parent["service"], s["service"])] += 1
    g = nx.DiGraph()
    g.add_nodes_from(services)
    for (a, b), n in calls.items():
        g.add_edge(a, b, calls=n)
    return g


def downstream_reach(g, service):
    """Services whose requests a failure of `service` could affect:
    walk edges AGAINST the call direction (callers, callers of callers)."""
    return nx.ancestors(g, service)
