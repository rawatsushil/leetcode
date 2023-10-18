# 2038. Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

"""
There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.
"""

"""
Solution1 - using Robin Karp
Time Complexity - O(m+n), where m is length of colors and n is length of pattern,
                Worst time complexity for Rabin karp is O(mn)
"""
class Solution:
    def __init__(self):
        self.chars = 256
        self.A = 'AAA'
        self.B = 'BBB'
        self.Q = 101

    def calculate_hash(self, txt):
        _hash = 0
        for i in range(len(txt)):
            _hash = (_hash*self.chars + ord(txt[i])) % self.Q
        return _hash % self.Q

    def check_string_match(self, str1, str2):
        for i in range(len(str1)):
            if not (str1[i] == str2[i]):
                return False
        return True

    def winnerOfGame(self, colors: str) -> bool:
        M = len(self.A)
        N = len(colors)

        count_a, count_b = 0, 0
        hash_a = self.calculate_hash(self.A)
        hash_b = self.calculate_hash(self.B)
        hash_text = self.calculate_hash(colors[:M])

        h = self.chars**(M-1)

        for i in range(N-M+1):

            if hash_a == hash_text:
                if self.check_string_match(colors[i:i+M], self.A):
                    count_a += 1
            elif hash_b == hash_text:
                if self.check_string_match(colors[i:i+M], self.B):
                    count_b += 1
            if i < N-M:
                hash_text = (
                    self.chars*(hash_text-ord(colors[i])*h) +
                    ord(colors[i+M])
                ) % self.Q
        return count_a > count_b



"""
Soution 2
Time complexity = O(n)
"""
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_a, count_b = 0, 0
        for i in range(1, len(colors)-1):
            if colors[i] == colors[i-1] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    count_a += 1
                else:
                    count_b += 1
        return count_a > count_b
