"""
Create a hash map stacks (or stack in TypeScript) that stores numbers as keys and their indices as values.
Iterate through nums with index i:
    Compute difference = target - nums[i].
    If difference is already in the map → we found the two indices, return [i, stacks[difference]].
    Otherwise, store nums[i] with its index in the map.
Since the problem guarantees exactly one solution, we can stop when found.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        stacks = {}

        for index in range(len(nums)):
            diffences = target - nums[index]

            if diffences in stacks:
                result.append(index)
                result.append(stacks[diffences])
                break

            stacks[nums[index]] = index

        return result
