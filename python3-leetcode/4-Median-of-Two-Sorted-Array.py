"""There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 == 0:
            return (nums3[len(nums3)//2-1]+nums3[len(nums3)//2])/2
        else:
            return (nums3[len(nums3)//2]) / 1
