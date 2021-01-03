def removeElement(nums, val):
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                nums.remove(nums[i])
            i -= 1
        return len(nums)
