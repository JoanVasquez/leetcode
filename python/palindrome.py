"""
Handle edge cases:
    Negative numbers are never palindromes (-121 ≠ 121-).
    Numbers ending in 0 but not equal to 0 are not palindromes (10 → "01" ≠ "10").
    0 is a palindrome by definition.
Convert the number to a string.
Find the middle index with floor(len/2).
Extract:
    Left half: from the beginning up to the middle.
    Right half: from the middle to the end, reversed.
Compare:
    If the two halves match → palindrome.
    If not, sometimes the left half has an extra digit (odd length case), so also compare leftHalf // 10 with rightHalf.
"""

import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        tmpX = str(x)
        mid = math.floor(len(tmpX) / 2)

        leftHalf = int(tmpX[0 : mid + 1])
        righHalf = int(tmpX[mid:])[::-1]

        return leftHalf == righHalf or math.floor(leftHalf / 10) == righHalf
