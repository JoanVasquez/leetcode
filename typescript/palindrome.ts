/*
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
 */

function isPalindrome(x: number): boolean {
  if (x === 0) return true;
  if (x < 0) return false;
  if (x % 10 === 0) return false;

  const tmpX = String(x);
  const mid = Math.floor(tmpX.length / 2);

  const leftHalf = parseInt(tmpX.slice(0, mid + 1));
  const rightHalf = parseInt(tmpX.slice(mid).split("").reverse().join(""));

  return leftHalf === rightHalf || Math.floor(leftHalf / 10) === rightHalf;
}
