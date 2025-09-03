/*
 Create a hash map stacks (or stack in TypeScript) that stores numbers as keys and their indices as values.
Iterate through nums with index i:
    Compute difference = target - nums[i].
    If difference is already in the map → we found the two indices, return [i, stacks[difference]].
    Otherwise, store nums[i] with its index in the map.
Since the problem guarantees exactly one solution, we can stop when found.
  */
function twoSum(nums: number[], target: number): number[] {
  const result: number[] = [];
  const stack: Record<number, number> = {};

  for (let index = 0; index < nums.length; index++) {
    const differences = target - nums[index];
    if (differences in stack) {
      result[0] = index;
      result[1] = stack[differences];
      break;
    }

    stack[nums[index]] = index;
  }

  return result;
}
