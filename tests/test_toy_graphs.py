"""Hand-computed toy graph. Expected values are derived on paper, not from the code.

Two traces:
  t1: frontend -> cart -> cache ; frontend -> checkout -> payment
  t2: frontend -> cart -> cache
Expected call counts: frontend->cart 2, cart->cache 2, frontend->checkout 1, checkout->payment 1.
Failure of 'cache' reaches cart and frontend (callers), not checkout or payment.
"""
from hdri.graph import build_graph, downstream_reach

def sp(t, s, p, svc):
    return dict(trace_id=t, span_id=s, parent_span_id=p, service=svc)

SPANS = [
    sp("t1", "a", None, "frontend"), sp("t1", "b", "a", "cart"), sp("t1", "c", "b", "cache"),
    sp("t1", "d", "a", "checkout"), sp("t1", "e", "d", "payment"),
    sp("t2", "a", None, "frontend"), sp("t2", "b", "a", "cart"), sp("t2", "c", "b", "cache"),
]

def test_call_counts():
    g = build_graph(SPANS)
    assert g["frontend"]["cart"]["calls"] == 2
    assert g["cart"]["cache"]["calls"] == 2
    assert g["frontend"]["checkout"]["calls"] == 1
    assert g["checkout"]["payment"]["calls"] == 1
    assert g.number_of_edges() == 4

def test_direction_is_caller_to_callee():
    g = build_graph(SPANS)
    assert g.has_edge("frontend", "cart") and not g.has_edge("cart", "frontend")

def test_failure_direction_is_opposite():
    g = build_graph(SPANS)
    assert downstream_reach(g, "cache") == {"cart", "frontend"}
    assert downstream_reach(g, "payment") == {"checkout", "frontend"}
    assert downstream_reach(g, "frontend") == set()

def test_same_service_spans_make_no_edge():
    spans = [sp("t", "a", None, "x"), sp("t", "b", "a", "x")]
    assert build_graph(spans).number_of_edges() == 0

def test_orphan_span_ignored():
    spans = [sp("t", "b", "missing", "y")]
    g = build_graph(spans)
    assert g.number_of_edges() == 0 and "y" in g
