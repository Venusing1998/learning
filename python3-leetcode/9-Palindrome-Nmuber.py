"""Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return int(str(x)[::-1]) == x