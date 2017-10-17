"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""





class Solution(object):

    @classmethod
    def findK(cls, l1, l2, k):
        print(l1, l2, k)
        if len(l1) > len(l2):
            return cls.findK(l2, l1, k)

        if len(l1) == 0:
            return l2[k - 1]
        elif k == 1:
            return min(l1[0], l2[0])

        else:
            p = min(k / 2, len(l1))
            q = k - p
            if l1[p - 1] < l2[q - 1]:
                return cls.findK(l1[p:], l2, k - p)
            elif l1[p - 1] == l2[q - 1]:
                return l1[p - 1]
            else:
                return cls.findK(l1, l2[q:], k - q)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)
        k = (m + n) / 2
        if (m + n) % 2 == 0:
            return ((self.findK(nums1, nums2, k) + self.findK(nums1, nums2, k + 1)) / 2.0)
        else:
            return self.findK(nums1, nums2, k + 1)

if __name__ == '__main__':
    Solution().findMedianSortedArrays([1, 2], [3, 4])
    Solution().findMedianSortedArrays([1, 3], [2])
