"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

    tips:
        sort the nums, use the last sum to figure out top or bottom to move
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        if len(nums) < 3:
            return []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:  # tips: all 0
                continue

            l = i + 1
            r = len(nums) - 1
            #             print(l,r)
            while l < r:
                sum_t = nums[i] + nums[l] + nums[r]
                if sum_t > 0:
                    r -= 1
                elif sum_t < 0:
                    l += 1
                else:
                    print(i, l, r)
                    result.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1
        return result
