# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""

"""
Note: Trick is to find left and right individually to keep code simple and clean
"""


class Solution:
    def search_binary(self, nums, target, find_left, find_right):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                if find_left:
                    if mid == lo or nums[mid - 1] < target:
                        return mid
                    hi = mid - 1
                else:
                    if mid == hi or nums[mid + 1] > target:
                        return mid
                    lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search_binary(nums, target, True, False)
        if left == -1:
            return [-1, -1]
        right = self.search_binary(nums, target, False, True)
        return [left, right]

