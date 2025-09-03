/*
 Edge Case Check: If the input array is empty, return an empty string immediately.
Initial Assumption: Initialize the prefix variable to be the first string in the array.
Iterate and Compare: For each subsequent word in the array:
    Use a while loop to check if the current word starts with the current prefix.
    If it doesn't, shorten the prefix by one character from the end (prefix.slice(0, -1)).
    If the prefix becomes empty at any point during this shortening, break out of the function and return an empty string.
Return Result: After successfully checking all words against the progressively shortened prefix, the remaining prefix is our answer.
 */

function longestCommonPrefix(strs: string[]): string {
  if (strs.length === 0) return "";

  let prefix = strs[0];

  for (const word of strs.slice(1)) {
    while (!word.startsWith(prefix)) {
      prefix = prefix.slice(0, -1);
      if (!prefix) return "";
    }
  }

  return prefix;
}
