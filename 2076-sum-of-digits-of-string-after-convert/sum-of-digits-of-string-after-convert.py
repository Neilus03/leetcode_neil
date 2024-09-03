class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert each character in the string to its corresponding number (1-26) 
        # and then split each number into its individual digits.
        indiv_number_list = [int(digit) for i in s for digit in str(ord(i) - 96)]

        # Perform the transformation k times
        for _ in range(k):
            # Sum all digits in the list
            res = sum(indiv_number_list)
            # Convert the sum back into individual digits for the next transformation
            indiv_number_list = [int(digit) for digit in str(res)]
        
        # Return the final result after k transformations
        return res
