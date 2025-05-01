import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.printer_queue import optimize_printing
import unittest

class TestPrinterQueue(unittest.TestCase):
    """
    Unit tests for the optimize_printing function.
    """
    def test_same_priority(self):
        """Test with jobs of the same priority."""
        jobs = [
            {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
            {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
        ]
        constraints = {"max_volume": 300, "max_items": 2}
        result = optimize_printing(jobs, constraints)
        self.assertEqual(result["print_order"], ["M2", "M1", "M3"])
        self.assertEqual(result["total_time"], 270)

    def test_different_priorities(self):
        """Test with jobs of different priorities."""
        jobs = [
            {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
            {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
        ]
        constraints = {"max_volume": 300, "max_items": 2}
        result = optimize_printing(jobs, constraints)
        self.assertEqual(result["print_order"], ["M2", "M1", "M3"])
        self.assertEqual(result["total_time"], 270)

    def test_exceeding_constraints(self):
        """Test with jobs exceeding printer constraints."""
        jobs = [
            {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
            {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
            {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
        ]
        constraints = {"max_volume": 300, "max_items": 2}
        result = optimize_printing(jobs, constraints)
        self.assertEqual(result["print_order"], ["M2", "M1", "M3"])
        self.assertEqual(result["total_time"], 450)

if __name__ == "__main__":
    unittest.main()
