# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/
"""
Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.
You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.
Return an integer array answer, where each answer[i] is the answer to the ith query.

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
"""

class Solution:
    @staticmethod
    def bisect_right(arr, val):
        lo, hi = 0, len(arr)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid] <= val:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


    @staticmethod
    def calculate_freq(word):
        word = "".join(sorted(word))
        word_count = Counter(word)
        return word_count[word[0]]

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        for i in range(len(words)):
            words[i] = self.calculate_freq(words[i])
        words.sort()
        for i in range(len(queries)):
            query_freq = self.calculate_freq(queries[i])
            pos = self.bisect_right(words, query_freq)
            ans.append(len(words) - pos)
        return ans