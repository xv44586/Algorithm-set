"""
Contains Duplicate III

Given an array of integers,
find out whether there are two distinct indices i and j in the array such that the absolute
difference between nums[i]
and nums[j] is at most t and the absolute difference between i and j is at most k.
"""

__doc__ = """
    abs(num[i] - num[j]) <= t ==>  abs(num[i]/t -num[j]/t) <= 1
    keep a order dict,key = num[i]/t, value=num[i],and keep the value length less or equals k
    for every num in nums, find is num/t or num/+1 or num -1 in dict and the diff of their value
    lt t

"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        from collections import OrderedDict
        key_bucket = OrderedDict()
        if len(nums) <= 1 or t < 0 or k < 1:
            return False

        for index, value in enumerate(nums):
            key = value // max(1, t)  # when t =0, value has to be same
            for kk in (key + 1, key, key - 1):
                if kk in key_bucket and abs(key_bucket[kk] - value) <= t:
                    return True

            key_bucket[key] = value
            if index >= k:
                key_bucket.popitem(last=False)
        return False