# hdri-thesis

Code, protocols and run logs for the master thesis "Design and Experimental Evaluation of the Hybrid Dependency Risk Index (HDRI) for Predictive Microservice Reliability in Hybrid Cloud Computing Environments".

| Folder | Purpose | Thesis chapter |
|---|---|---|
| slr/ | Review protocol, search strings, screening and counts | 1 |
| experiments/ | Run manifest schema, run matrix | 2 |
| freeze/ | Signed, dated specification (git-tagged before final runs) | 2, 5 |
| hdri/ | HDRI library (graph, impact, warning, risk) | 3, 4 |
| tests/ | Toy-graph and synthetic-telemetry tests | 3, 4 |
| calibration/ | Pilot-only fitting | 3 |
| infra/ deploy/ observability/ probes/ load/ chaos/ | Testbed, application, telemetry, load and faults | 4 |
| analysis/ | Analysis scripts, run only after the freeze | 5 |
| docs/ | AI-use log, iteration log, evidence register | all |

## Rules
1. Pilot runs are never used in final estimates.
2. After the freeze tag, no design change; findings are reported, not fixed.
3. Every figure and table in Chapter 5 must regenerate from raw run logs.
4. No secrets (tokens, keys, VPN passwords) in the repository.

## Quick start
    pip install -r requirements.txt
    pytest
