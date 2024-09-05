import numpy as np
from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Calculate the total required sum for both given rolls and missing rolls
        m = len(rolls)
        total_sum_needed = mean * (m + n)
        current_sum = sum(rolls)
        missing_sum = total_sum_needed - current_sum
        
        # Check if the missing_sum can be divided into n rolls with values between 1 and 6
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        changing_rolls = [1] * n


        i = 0
        extra_need = missing_sum - n  # Subtract n because each die is initialized to 1
        while extra_need > 0:
            # Increment the current dice by 1 until it's 6 or we've used all extra_need
            while changing_rolls[i] < 6 and extra_need > 0:
                changing_rolls[i] += 1
                extra_need -= 1
                
            i += 1  # Move to the next die

        return changing_rolls
