"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count1 = nums[0], 1
        for i in range(1, len(nums)):
            if count1 == 0:
                candidate, count1 = nums[i], 1
            elif nums[i] == candidate:
                count1 += 1
            else:
                count1 -= 1
        return candidate