"""Reproducible scoring calculation tests, not AI-behavior tests."""
import importlib.util
import pathlib
import unittest

PATH = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "score.py"
spec = importlib.util.spec_from_file_location("second_look_score", PATH)
score_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(score_module)
score = score_module.score


class ScoreTest(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(score(dict.fromkeys("abcde", 5))["score_out_of_10"], 10.0)

    def test_all_four(self):
        self.assertEqual(score(dict.fromkeys("abcde", 4))["score_out_of_10"], 8.0)

    def test_weights(self):
        self.assertEqual(score(dict(a=5, b=4, c=4, d=4, e=4))["score_out_of_10"], 8.5)

    def test_round_half_up(self):
        self.assertEqual(score(dict(a=4, b=4, c=4, d=4, e=4.5))["score_out_of_10"], 8.2)

    def test_fractions_rejected(self):
        with self.assertRaises(ValueError):
            score(dict(a=4.3, b=4, c=4, d=4, e=4))

    def test_non_numeric_rejected(self):
        with self.assertRaises(ValueError):
            score(dict(a="invalid", b=4, c=4, d=4, e=4))

    def test_not_finite_rejected(self):
        with self.assertRaises(ValueError):
            score(dict(a="NaN", b=4, c=4, d=4, e=4))

    def test_missing_dimension_rejected(self):
        with self.assertRaises(ValueError):
            score(dict(a=4, b=4, c=4, d=4))

    def test_out_of_range_rejected(self):
        with self.assertRaises(ValueError):
            score(dict(a=6, b=4, c=4, d=4, e=4))


if __name__ == "__main__":
    unittest.main()
