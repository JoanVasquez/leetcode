'''
Edge Case Check: If the input array is empty, return an empty string immediately.
Initial Assumption: Initialize the prefix variable to be the first string in the array.
Iterate and Compare: For each subsequent word in the array:
    Use a while loop to check if the current word starts with the current prefix.
    If it doesn't, shorten the prefix by one character from the end (prefix.slice(0, -1)).
    If the prefix becomes empty at any point during this shortening, break out of the function and return an empty string.
Return Result: After successfully checking all words against the progressively shortened prefix, the remaining prefix is our answer.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) --> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""

        return prefix
