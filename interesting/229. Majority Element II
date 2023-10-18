"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, candidate1 = 0, None
        count2, candidate2 = 0, None

        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1 += 1
            elif nums[i] == candidate2:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                candidate1 = nums[i]
            elif count2 == 0:
                count2 += 1
                candidate2 = nums[i]
            else:
                count1 -= 1
                count2 -= 1
        ans = [
            num for num in [candidate1, candidate2] if nums.count(num) > len(nums)//3
        ]
        return ans

