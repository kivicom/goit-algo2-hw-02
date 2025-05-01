import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.rod_cutting import rod_cutting_memo, rod_cutting_table
import unittest

class TestRodCutting(unittest.TestCase):
    """
    Unit tests for the rod cutting functions.
    """
    def test_basic_case_memo(self):
        """Test memoization with basic case."""
        result = rod_cutting_memo(5, [2, 5, 7, 8, 10])
        self.assertEqual(result["max_profit"], 12)
        self.assertEqual(sum(result["cuts"]), 5)
        self.assertEqual(result["number_of_cuts"], len(result["cuts"]) - 1 if result["cuts"] else 0)

    def test_basic_case_table(self):
        """Test tabulation with basic case."""
        result = rod_cutting_table(5, [2, 5, 7, 8, 10])
        self.assertEqual(result["max_profit"], 12)
        self.assertEqual(sum(result["cuts"]), 5)
        self.assertEqual(result["number_of_cuts"], len(result["cuts"]) - 1 if result["cuts"] else 0)

    def test_no_cut_memo(self):
        """Test memoization with optimal no-cut case."""
        result = rod_cutting_memo(3, [1, 3, 8])
        self.assertEqual(result["max_profit"], 8)
        self.assertEqual(result["cuts"], [3])
        self.assertEqual(result["number_of_cuts"], 0)

    def test_no_cut_table(self):
        """Test tabulation with optimal no-cut case."""
        result = rod_cutting_table(3, [1, 3, 8])
        self.assertEqual(result["max_profit"], 8)
        self.assertEqual(result["cuts"], [3])
        self.assertEqual(result["number_of_cuts"], 0)

    def test_uniform_cuts_memo(self):
        """Test memoization with uniform cuts."""
        result = rod_cutting_memo(4, [3, 5, 6, 7])
        self.assertEqual(result["max_profit"], 12)
        self.assertEqual(result["cuts"], [1, 1, 1, 1])
        self.assertEqual(result["number_of_cuts"], 3)

    def test_uniform_cuts_table(self):
        """Test tabulation with uniform cuts."""
        result = rod_cutting_table(4, [3, 5, 6, 7])
        self.assertEqual(result["max_profit"], 12)
        self.assertEqual(result["cuts"], [1, 1, 1, 1])
        self.assertEqual(result["number_of_cuts"], 3)

if __name__ == "__main__":
    unittest.main()