import unittest

from password_strength.checker import check_password


class CheckPasswordTests(unittest.TestCase):
    def test_strong_password_gets_full_score(self) -> None:
        result = check_password("Correct-Horse-42!")
        self.assertEqual(result.score, 5)
        self.assertEqual(result.label, "Strong")
        self.assertFalse(result.tips)

    def test_short_password_reports_length_and_variety_tips(self) -> None:
        result = check_password("abc")
        self.assertLess(result.score, 3)
        self.assertTrue(any("8 characters" in tip for tip in result.tips))
        self.assertTrue(any("character types" in tip or "character" in tip for tip in result.tips))

    def test_common_password_is_penalized_case_insensitively(self) -> None:
        result = check_password("PASSWORD")
        self.assertTrue(result.is_common)
        self.assertEqual(result.score, 1)
        self.assertIn("common passwords", result.tips[0])


if __name__ == "__main__":
    unittest.main()
