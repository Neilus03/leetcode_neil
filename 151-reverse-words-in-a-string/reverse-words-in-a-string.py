class Solution(object):
    def reverseWords(self, s):
        # Join the reversed words with spaces
        return ' '.join(s.split()[::-1])
        