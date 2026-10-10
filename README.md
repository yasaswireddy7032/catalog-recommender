# Catalog Recommender

[![Tests](https://github.com/yasaswireddy7032/catalog-recommender/actions/workflows/tests.yml/badge.svg)](https://github.com/yasaswireddy7032/catalog-recommender/actions)

Item-item collaborative filtering with seen-item exclusion, popularity fallback, and holdout ranking evaluation.

**Status:** runnable portfolio reference implementation. Uses synthetic or hand-authored demonstration data. No employer code, customer data, or production performance claims.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
python -m unittest -v
```

The default command prints a reproducible JSON demonstration. See `app.py` for the reusable Python API. `example-output.json` records the locally executed demo; it is not an external benchmark.

## Architecture

Unique user-item interactions → item co-occurrence cosine → candidate scoring → seen-item exclusion → deterministic ranking. The evaluator rejects overlapping train/holdout interactions.

## Validation

Tests exercise failure cases and behavioral invariants, in addition to the executable demo. GitHub Actions runs the tests and demo on pushes and pull requests. See the Actions tab for current results.

## Limitations and next steps

Tiny hand-authored demo, no production relevance claim. Item similarity is expensive for large catalogs; add sparse matrices or approximate neighbors. Use time-based holdout, cold-start metadata, diversity constraints, and exposure-aware evaluation.

## Container

```bash
docker build -t catalog-recommender .
docker run --rm catalog-recommender
```

The Docker recipe is provided; local validation uses Python, not Docker.

## Responsible use

Review the code and understand its assumptions before deploying. Keep credentials in environment variables and exclude private data from commits. This project is an educational engineering baseline, not a production-certified service.
