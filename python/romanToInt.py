"""
Create a mapping of Roman numerals to integers.
Initialize total = 0 and prev = 0.
Traverse the string backwards:
    Convert the character into its numeric value.
    If it’s smaller than the previous numeral → subtract it.
    Otherwise → add it.
    Update prev.
Return total.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        total = 0
        prev = 0

        for char in reversed(s):
            current = roman_nums[char]
            total += -current if current < prev else current
            prev = current

        return total
