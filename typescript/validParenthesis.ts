/*
Immediately reject if the string has odd length or starts/ends with an invalid bracket (quick boundary check).
Use a stack:
    Push opening brackets onto the stack.
    When encountering a closing bracket:
        If the stack is empty → invalid.
        Pop from the stack and ensure it matches the closing bracket using a mapping.
At the end, the stack must be empty for the string to be valid.
 */

function isValid(s: string): boolean {
  const n = s.length;
  if (n & 1) return false; // odd length can't be valid

  // Quick boundary rejects (short-circuit early)
  const first = s[0],
    last = s[n - 1];
  if (first === ")" || first === "]" || first === "}") return false;
  if (last === "(" || last === "[" || last === "{") return false;

  const stack: string[] = [];
  const match: Record<string, string> = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  for (let i = 0; i < n; i++) {
    const ch = s[i];
    if (ch === "(" || ch === "[" || ch === "{") {
      stack.push(ch);
    } else {
      if (stack.length === 0 || stack.pop() !== match[ch]) {
        return false;
      }
    }
  }

  return stack.length === 0;
}
