from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    """
    Represents a 3D printing job with its attributes.
    """
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    """
    Represents the constraints of the 3D printer.
    """
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Optimizes the 3D printing queue based on priorities and printer constraints using a greedy approach.

    Args:
        print_jobs: List of printing jobs, each with id, volume, priority, and print_time.
        constraints: Printer constraints with max_volume and max_items.

    Returns:
        Dict with the print order and total printing time.
    """
    # Convert input dictionaries to PrintJob and PrinterConstraints objects
    jobs = [PrintJob(**job) for job in print_jobs]
    printer = PrinterConstraints(**constraints)
    
    # Sort jobs by priority (ascending, so 1 is highest) and then by print_time (ascending)
    jobs.sort(key=lambda x: (x.priority, x.print_time))
    
    print_order = []
    total_time = 0
    
    # Process jobs greedily
    i = 0
    while i < len(jobs):
        # Collect jobs for the current batch
        batch = []
        batch_volume = 0
        j = i
        
        # Try to add jobs to the batch while respecting constraints
        while j < len(jobs) and len(batch) < printer.max_items:
            if batch_volume + jobs[j].volume <= printer.max_volume:
                batch.append(jobs[j])
                batch_volume += jobs[j].volume
            j += 1
        
        # If no jobs can be added to the batch, process the current job alone
        if not batch:
            batch = [jobs[i]]
            i += 1
        
        # Calculate batch time as the maximum print time in the batch
        batch_time = max(job.print_time for job in batch)
        total_time += batch_time
        
        # Add batch job IDs to the print order
        print_order.extend(job.id for job in batch)
        
        # Move index to the next unprocessed job
        i = max(i + len(batch), i + 1)
    
    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Test cases
if __name__ == "__main__":
    def test_printing_optimization():
        """Test the optimize_printing function with provided test cases."""
        # Test 1: Same priority
        test1_jobs = [
            {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
            {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
        ]

        # Test 2: Different priorities
        test2_jobs = [
            {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
            {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
            {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
        ]

        # Test 3: Exceeding constraints
        test3_jobs = [
            {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
            {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
            {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
        ]

        constraints = {
            "max_volume": 300,
            "max_items": 2
        }

        print("Test 1 (same priority):")
        result1 = optimize_printing(test1_jobs, constraints)
        print(f"Print order: {result1['print_order']}")
        print(f"Total time: {result1['total_time']} minutes")

        print("\nTest 2 (different priorities):")
        result2 = optimize_printing(test2_jobs, constraints)
        print(f"Print order: {result2['print_order']}")
        print(f"Total time: {result2['total_time']} minutes")

        print("\nTest 3 (exceeding constraints):")
        result3 = optimize_printing(test3_jobs, constraints)
        print(f"Print order: {result3['print_order']}")
        print(f"Total time: {result3['total_time']} minutes")

    test_printing_optimization()