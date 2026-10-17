<!-- oss-factory:v1
{"id":"20261017-civic-allusgov-queue","kind":"state","project":"allusgov","from":"chatgpt","to":["factory"],"status":"working","dedupe_key":"promotion-queue:CivicActions/allusgov","civ":{"city_id":"oss:allusgov"}}
-->

# Canonical upstream promotion queue — CivicActions/allusgov

Tracked via registry PR https://github.com/kvnloo/oss-factory/pull/191 (provisional until merged). Fork Issues are disabled; this fork-local document is the **one canonical queue**. Original implementation PRs, issue threads, and author credit stay where they originated.

- Origin: https://github.com/CivicActions/allusgov
- Coordination fork: https://github.com/kvnloo/allusgov
- Last evidence audit: 2026-10-17
- State: **ORIGIN_LIVE / CHECK** (not origin-action authorization)

## Existing upstream review / source work

- Origin PR: https://github.com/CivicActions/allusgov/pull/38 (draft; no reviews yet).
- Maintainer-reported requirement: https://github.com/CivicActions/allusgov/issues/25 (source provenance during merged government directories).
- Source: `civic/provenance-25` @ `5f9dac8cc750fb95ebf6b28813500bab83adc157`.
- Regression: sequential three-source merge; text, JSON, CSV assertions committed. **Full native tests not run**.
- CI: https://github.com/CivicActions/allusgov/actions/runs/39076013202 — `action_required`, **zero jobs**, not green. Requested optional maintainer workflow approval once on the existing PR: https://github.com/CivicActions/allusgov/pull/38#issuecomment-6243118440.
- Gate: execute Python 3.12 `uv sync`, `uv run pytest`, full configured lint; resolve any regression and CI comments on **the same origin PR**.
- Next: source-level test integrity review, request workflow approval only if necessary; mark ready only after verified checks.

## Release gates

- Record original author/reporter/maintainer provenance and exact source head SHA.
- Follow project contribution policy, current upstream reviews, conflicts, and CI checks.
- Require native targeted tests; separate static reasoning from exercised runtime evidence.
- Do not publish an overlapping origin PR or claim a fork draft is landed.
- Only a bounded human authorization under factory/HITL.md permits additional origin actions; upstream merges are for maintainers.

## Results

- **Ready for new origin publication:** none independently verified.
- **Origin writes from this coordination update:** none.
- **Next update:** when CI/reviews/test results or upstream ownership changes materially.
