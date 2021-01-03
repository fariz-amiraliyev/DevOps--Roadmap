def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not len(set(nums))==len(nums)
