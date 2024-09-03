class Solution:
    def reverse(self, x: int) -> int:
        # Reverse the integer as a string, handle the negative sign if present
        reversed_num = int(str(-x)[::-1]) if x < 0 else int(str(x)[::-1])
        
        # Check if the original number was negative
        neg = x < 0

        # Return 0 if the reversed number is out of 32-bit integer range
        if reversed_num >= 2**31 - 1 or reversed_num < -2**31:
            return 0

        # Return the reversed number with the correct sign
        return -reversed_num if neg else reversed_num
