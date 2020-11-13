const n = nums.length;
const expectedSum = (n * (n + 1)) / 2;
const sum = nums.reduce((total, num) => total += num, 0);
return expectedSum - sum;
