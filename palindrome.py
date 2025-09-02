"""
create a function that receive a var named num, for example 121
create variable named result with a value of ''
if num < 0: return False

121 turn this number to string
loop over the new string 121

result = 1 = 1
result = 2 + 1 = 21
result = 1 + 2 + 1 = 121
loop done

return int(result) == num

"""

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x == 0:
#             return True
#         if x < 0:
#             return False
#         if x % 10 == 0:
#             return False
#
#         result = ""
#
#         for char in str(x):
#             result = char + result
#
#         return int(result) == true

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
