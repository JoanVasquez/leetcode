"""
Immediately reject if the string has odd length or starts/ends with an invalid bracket (quick boundary check).
Use a stack:
    Push opening brackets onto the stack.
    When encountering a closing bracket:
        If the stack is empty → invalid.
        Pop from the stack and ensure it matches the closing bracket using a mapping.
At the end, the stack must be empty for the string to be valid.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:  # odd length can't be valid
            return False

        # Quick boundary rejects (often short-circuit early)
        if s[0] in ")]}" or s[-1] in "([{":
            return False

        stack: list[str] = []
        match = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in "([{":  # opening
                stack.append(ch)
            else:  # closing
                if not stack or stack.pop() != match[ch]:
                    return False

        return not stack
