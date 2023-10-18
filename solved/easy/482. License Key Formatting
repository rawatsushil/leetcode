# https://leetcode.com/problems/license-key-formatting/description/
""""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
Return the reformatted license key.

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        list_s = []
        count = 0
        for i in range(len(s)):
            if s[i] != "-":
                list_s.append(s[i].upper())
                count += 1
        new_s = "".join(list_s)
        list_s = []
        rem = count % k
        if rem:
            list_s.append(new_s[:rem])
        i = rem
        while i < len(new_s):
            list_s.append(new_s[i:i+k])
            i = i+k
        return "-".join(list_s)
