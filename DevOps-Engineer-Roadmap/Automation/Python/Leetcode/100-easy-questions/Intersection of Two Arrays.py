Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


My solution:
if len(nums1) >= len(nums2):
    for x in set(nums2):
        if x in set(nums1):
            print(x)
else:
    for y in set(nums1):
        if y in set(nums2):
            print(y)


# One line solution:

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1).intersection(nums2)


Or

from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(Counter(nums1) & Counter(nums2))
