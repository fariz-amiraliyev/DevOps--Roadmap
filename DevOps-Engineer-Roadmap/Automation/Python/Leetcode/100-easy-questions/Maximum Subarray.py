Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

 def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        last_max = nums[0]

        for i in xrange(len(nums)):
            if i==0: continue
            last_max = max(nums[i], nums[i]+last_max)
            ans = max(ans, last_max)

        return ans
