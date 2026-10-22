# SLR search strings (Chapter 1, Section 1.6.1)
Window: 2017-2026. Run each database ONCE; record the date and hit count below. Export to CSV/RIS with title, authors, year, DOI, abstract.

Groups
- A (microservices): microservice* OR "micro-service*"
- B (reliability): reliab* OR failure OR fault OR anomal* OR degrad* OR SLO OR resilien*
- C (dependency/tracing): dependenc* OR "call graph" OR "service graph" OR trace OR tracing
- D (environment boundary): "hybrid cloud" OR "multi-cloud" OR "multi-cluster" OR "edge-cloud" OR "cross-cloud" OR "wide-area" OR "network latency"

Core string = A AND B AND C. Exposure string = A AND B AND D. Screen the union.

## Per-database syntax (check each interface; syntax changes)
**Scopus** (Advanced search):
TITLE-ABS-KEY((microservice* OR "micro-service*") AND (reliab* OR failure OR fault OR anomal* OR degrad* OR slo OR resilien*) AND (dependenc* OR "call graph" OR "service graph" OR trace OR tracing)) AND PUBYEAR > 2016 AND PUBYEAR < 2027
(repeat with group D in place of C)

**IEEE Xplore** (Command search):
("Abstract":microservice* OR "Abstract":"micro-service*") AND ("Abstract":reliab* OR "Abstract":failure OR "Abstract":fault OR "Abstract":anomal* OR "Abstract":degrad* OR "Abstract":SLO OR "Abstract":resilien*) AND ("Abstract":dependenc* OR "Abstract":"call graph" OR "Abstract":"service graph" OR "Abstract":trace OR "Abstract":tracing)
Filter years 2017-2026.

**ACM Digital Library** (Advanced search, Abstract field):
Abstract:(microservice* OR "micro-service*") AND Abstract:(reliab* OR failure OR fault OR anomal* OR degrad* OR SLO OR resilien*) AND Abstract:(dependenc* OR "call graph" OR "service graph" OR trace OR tracing); filter 2017-2026.

**SpringerLink**: simple query with the same groups and the date filter 2017-2026 (the interface limits wildcard use; list word variants explicitly).

**arXiv** (cs.SE, cs.DC): search abstracts for "microservice" AND (dependency OR "call graph") AND (failure OR anomaly OR reliability); sort by date; preprints only.

## Run log (fill in)
| Database | String | Date run | Hits | Exported file |
|---|---|---|---|---|
| Scopus | core | | | |
| Scopus | exposure | | | |
| IEEE Xplore | core | | | |
| IEEE Xplore | exposure | | | |
| ACM DL | core | | | |
| ACM DL | exposure | | | |
| SpringerLink | core | | | |
| SpringerLink | exposure | | | |
| arXiv | combined | | | |
