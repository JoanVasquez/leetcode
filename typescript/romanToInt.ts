/*
 Create a mapping of Roman numerals to integers.
Initialize total = 0 and prev = 0.
Traverse the string backwards:
    Convert the character into its numeric value.
    If it’s smaller than the previous numeral → subtract it.
    Otherwise → add it.
    Update prev.
Return total.
 */

function romanToInt(s: string): number {
  const romanNums: Record<string, number> = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let total = 0;
  let prev = 0;

  // Loop from right to left
  for (let i = s.length - 1; i >= 0; i--) {
    const char = s[i];
    const current = romanNums[char];

    if (current < prev) {
      total -= current;
    } else {
      total += current;
    }

    prev = current;
  }

  return total;
}
