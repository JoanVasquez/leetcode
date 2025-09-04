/*
 At each step:
    If the digit is less than 9, just increment it and return (no carry needed).
    If the digit is 9, set it to 0 and continue the loop (carry over).
If we exit the loop, it means all digits were 9, so we return [1] + digits (new leading 1 followed by zeros).
 */

function plusOne(digits: number[]): number[] {
  for (let index = digits.length - 1; index >= 0; index--) {
    if (digits[index] < 9) {
      digits[index] += 1;
      return digits;
    }
    digits[index] = 0;
  }

  digits.unshift(1);
  return digits;
}
