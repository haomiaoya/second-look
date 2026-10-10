#!/usr/bin/env python3
"""Deterministic scoring for second-look. Standard library only."""
import argparse
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

WEIGHTS = {"a": 25, "b": 25, "c": 20, "d": 15, "e": 15}


def score(values):
    """Return the weighted score (out of 10). All five dimensions are required."""
    if set(values) != set(WEIGHTS):
        raise ValueError("Must provide all five dimensions: a, b, c, d, e")
    try:
        dec = {key: Decimal(str(val)) for key, val in values.items()}
    except (InvalidOperation, TypeError) as exc:
        raise ValueError("All dimension scores must be numeric") from exc
    for key, value in dec.items():
        if not value.is_finite() or not (0 <= value <= 5) or value * 2 != (value * 2).to_integral_value():
            raise ValueError(f"{key} must be finite, between 0 and 5, in steps of 0.5")
    total = sum((dec[k] * weight for k, weight in WEIGHTS.items()), Decimal(0)) / 50
    total = total.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    return {
        "dimensions": {k.upper(): float(dec[k]) for k in WEIGHTS},
        "weights": {k.upper(): w for k, w in WEIGHTS.items()},
        "score_out_of_10": float(total),
    }


def main():
    parser = argparse.ArgumentParser(description="Calculate second-look weighted score")
    for key in WEIGHTS:
        parser.add_argument(f"--{key}", required=True, type=str, help="0..5 in 0.5 increments")
    args = parser.parse_args()
    try:
        result = score({k: getattr(args, k) for k in WEIGHTS})
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
