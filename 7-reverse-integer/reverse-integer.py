class Solution:
    def reverse(self, x: int) -> int:
        # Reverse the integer as a string, handle the negative sign if present
        reversed_num = int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
        
        # Return 0 if the reversed number is out of 32-bit integer range
        if abs(reversed_num) >= 2**31 - 1:
            return 0

        # Return the reversed number with the correct sign
        return -reversed_num if x < 0 else reversed_num
