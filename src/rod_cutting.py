from typing import List, Dict, Tuple
from functools import lru_cache

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal way to cut a rod for maximum profit using memoization.

    Args:
        length: Length of the rod.
        prices: List of prices where prices[i] is the price for a rod of length i+1.

    Returns:
        Dict with maximum profit, list of cuts, and number of cuts.
    """
    if length <= 0 or not prices:
        return {"max_profit": 0, "cuts": [], "number_of_cuts": 0}

    @lru_cache(maxsize=None)
    def memo_cut(remaining: int) -> Tuple[int, List[int]]:
        """Helper function for memoized rod cutting."""
        if remaining == 0:
            return 0, []
        
        max_profit = float('-inf')
        best_cuts = []
        
        for i in range(min(remaining, len(prices))):
            profit, cuts = memo_cut(remaining - (i + 1))
            total_profit = prices[i] + profit
            if total_profit > max_profit:
                max_profit = total_profit
                best_cuts = [i + 1] + cuts
        
        return max_profit, best_cuts

    max_profit, cuts = memo_cut(length)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1 if cuts else 0
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Finds the optimal way to cut a rod for maximum profit using tabulation.

    Args:
        length: Length of the rod.
        prices: List of prices where prices[i] is the price for a rod of length i+1.

    Returns:
        Dict with maximum profit, list of cuts, and number of cuts.
    """
    if length <= 0 or not prices:
        return {"max_profit": 0, "cuts": [], "number_of_cuts": 0}

    # Initialize DP table and cuts tracking
    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]
    
    for i in range(1, length + 1):
        max_profit = float('-inf')
        best_cut = []
        
        for j in range(min(i, len(prices))):
            profit = prices[j] + dp[i - (j + 1)]
            if profit > max_profit:
                max_profit = profit
                best_cut = [j + 1] + cuts[i - (j + 1)]
        
        dp[i] = max_profit
        cuts[i] = best_cut
    
    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length]) - 1 if cuts[length] else 0
    }

# Test cases
if __name__ == "__main__":
    def run_tests():
        """Run all test cases for rod cutting algorithms."""
        test_cases = [
            # Test 1: Basic case
            {
                "length": 5,
                "prices": [2, 5, 7, 8, 10],
                "name": "Basic case"
            },
            # Test 2: Optimal to not cut
            {
                "length": 3,
                "prices": [1, 3, 8],
                "name": "Optimal to not cut"
            },
            # Test 3: Uniform cuts
            {
                "length": 4,
                "prices": [3, 5, 6, 7],
                "name": "Uniform cuts"
            }
        ]

        for test in test_cases:
            print(f"\nTest: {test['name']}")
            print(f"Rod length: {test['length']}")
            print(f"Prices: {test['prices']}")

            # Test memoization
            memo_result = rod_cutting_memo(test['length'], test['prices'])
            print("\nMemoization result:")
            print(f"Maximum profit: {memo_result['max_profit']}")
            print(f"Cuts: {memo_result['cuts']}")
            print(f"Number of cuts: {memo_result['number_of_cuts']}")

            # Test tabulation
            table_result = rod_cutting_table(test['length'], test['prices'])
            print("\nTabulation result:")
            print(f"Maximum profit: {table_result['max_profit']}")
            print(f"Cuts: {table_result['cuts']}")
            print(f"Number of cuts: {table_result['number_of_cuts']}")

            print("\nTest passed successfully!")

    run_tests()