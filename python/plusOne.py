"""
Traverse the digits from right to left (least significant to most significant).
At each step:
    If the digit is less than 9, just increment it and return (no carry needed).
    If the digit is 9, set it to 0 and continue the loop (carry over).
If we exit the loop, it means all digits were 9, so we return [1] + digits (new leading 1 followed by zeros).
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for index in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
