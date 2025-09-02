"""
result a list empty
stacks a dictionary empty

[2,11,7,15], 9
9 - 2 = 7, 7 in stacks ? no dictory is empty
then: stacks { 2 : 0 }

9 - 11 = -2, -2 in stacks ? no, stacks has { 2 : 0 }
then: stacks { 2 : 0, 11 : 1 }

9 - 7 = 2, 2 in stacks ? si, stacks has { 2 : 0, 11 : 1 }
then: add to result current index = 2, also add stacks[2] = 0

return result

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
