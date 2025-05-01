# Homework: Greedy Algorithms and Dynamic Programming

## Overview

This project implements two algorithms as part of a homework assignment on greedy algorithms and dynamic programming:

1. **Task 1: Optimize 3D Printer Queue**

   - Function: `optimize_printing`
   - Optimizes a 3D printing queue based on priorities and printer constraints using a greedy approach.
   - Features: Groups jobs for simultaneous printing, prioritizes higher-priority tasks, respects volume and item constraints.
   - Time complexity: O(n log n) due to sorting.

2. **Task 2: Optimal Rod Cutting**

   - Functions: `rod_cutting_memo`, `rod_cutting_table`
   - Finds the optimal way to cut a rod for maximum profit using dynamic programming (memoization and tabulation).
   - Time complexity: O(n²) for both approaches.

## Project Structure

- `src/`
  - `__init__.py`: Marks the directory as a Python package.
  - `printer_queue.py`: Implementation of the 3D printer queue optimization (Task 1).
  - `rod_cutting.py`: Implementation of the rod cutting algorithms (Task 2).
- `tests/`
  - `__init__.py`: Marks the directory as a Python package.
  - `test_printer_queue.py`: Unit tests for Task 1.
  - `test_rod_cutting.py`: Unit tests for Task 2.
- `requirements.txt`: List of dependencies (pytest).
- `README.md`: This file, containing project documentation.
- `.gitignore`: Ignores unnecessary files (e.g., .venv, __pycache__).

## Requirements

- **Python**: 3.8 or higher
- **Dependencies**:
  - No external dependencies required if using `unittest`.
  - Optional: `pytest` for running tests.

    ```
    pip install -r requirements.txt
    ```

## Setup

1. Clone or download the project repository.
2. (Optional) Create and activate a virtual environment:

   ```
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```
3. Install dependencies (if using pytest):

   ```
   pip install -r requirements.txt
   ```

## Running the Code

- **Task 1 (printer_queue)**:

  ```
  python src/printer_queue.py
  ```

  Example output:

  ```
  Test 1 (same priority):
  Print order: ['M2', 'M1', 'M3']
  Total time: 270 minutes

  Test 2 (different priorities):
  Print order: ['M2', 'M1', 'M3']
  Total time: 270 minutes

  Test 3 (exceeding constraints):
  Print order: ['M2', 'M1', 'M3']
  Total time: 450 minutes
  ```

- **Task 2 (rod_cutting)**:

  ```
  python src/rod_cutting.py
  ```

  Example output:

  ```
  Test: Basic case
  Rod length: 5
  Prices: [2, 5, 7, 8, 10]
  Memoization result:
  Maximum profit: 12
  Cuts: [1, 2, 2]
  Number of cuts: 2
  Tabulation result:
  Maximum profit: 12
  Cuts: [2, 2, 1]
  Number of cuts: 2

  Test: Optimal to not cut
  Rod length: 3
  Prices: [1, 3, 8]
  Memoization result:
  Maximum profit: 8
  Cuts: [3]
  Number of cuts: 0
  Tabulation result:
  Maximum profit: 8
  Cuts: [3]
  Number of cuts: 0

  Test: Uniform cuts
  Rod length: 4
  Prices: [3, 5, 6, 7]
  Memoization result:
  Maximum profit: 12
  Cuts: [1, 1, 1, 1]
  Number of cuts: 3
  Tabulation result:
  Maximum profit: 12
  Cuts: [1, 1, 1, 1]
  Number of cuts: 3
  ```

## Running Tests

Tests are implemented using `unittest` and can also be run with `pytest`.

- **Using unittest**:

  ```
  python -m unittest discover tests
  ```

- **Using pytest** (recommended):

  ```
  PYTHONPATH=. pytest tests/
  ```

  Note: The `PYTHONPATH=.` ensures the `src` module is found. Test files include `sys.path` modifications to handle imports.

  Example output:

  ```
  collected 9 items
  tests/test_printer_queue.py ... [ 33%]
  tests/test_rod_cutting.py ...... [100%]
  ```

## Notes

- **Task 1**: The greedy algorithm sorts jobs by priority and print time, grouping them into batches while respecting printer constraints. Batch time is the maximum print time among jobs in the batch.
- **Task 2**: Both memoization and tabulation approaches solve the rod cutting problem efficiently, tracking the maximum profit and the list of cuts.
- **Improvements**: For `optimize_printing`, consider optimizing batch selection for edge cases. For `rod_cutting`, additional input validation could be added.
- **Testing**: Tests cover all required scenarios, including same/different priorities, constraint violations, and various rod cutting cases.

## Troubleshooting

- **ModuleNotFoundError**: If you encounter `No module named 'src'`, ensure:
  - The `__init__.py` files exist in `src/` and `tests/`.
  - Use `PYTHONPATH=.` when running pytest, or verify that test files include `sys.path` modifications.
- **Contact**: If issues persist, reach out to the mentor via Slack.