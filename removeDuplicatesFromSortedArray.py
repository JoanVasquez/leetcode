"""
Use two pointers:
i → reader, scans every element in the array.
k → writer, marks the position of the next unique element.
Start with k = 1 because the first element is always unique.
For each element at index i:
If it is different from the last unique (nums[k-1]), we place it at nums[k] and increment k.
At the end, the first k positions contain all unique elements in order, and we return k.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

    k = 1

    for index in range(1, len(nums)):
        if nums[index] != nums[k - 1]:
            nums[k] = nums[index]
            k += 1

    return k
