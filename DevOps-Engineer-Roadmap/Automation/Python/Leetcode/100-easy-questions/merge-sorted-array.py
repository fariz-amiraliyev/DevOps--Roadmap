class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """    """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        end_1 = m - 1
        end_2 = n - 1
        fill_idx = (m + n) - 1

        while fill_idx >= 0:

            if nums1[end_1] < nums2[end_2] or end_1 < 0:
                nums1[fill_idx] = nums2[end_2]
                nums2[end_2] = 0
                end_2 -= 1
            else:
                nums1[fill_idx] = nums1[end_1]
                nums1[end_1] = 0
                end_1 -= 1

            if end_2 < 0:
                return

            fill_idx -= 1
