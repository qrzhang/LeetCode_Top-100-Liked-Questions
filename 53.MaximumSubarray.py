class Solution:
    def maxSubArray(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        if len(nums) == 1:
            return nums
        SumMax = nums[0]
        current = nums[0]
        for i, num in enumerate(nums):
            if current < 0:
                current = num
            else:
                current += num
            if current > SumMax:
                SumMax = current
        return SumMax


nums = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution()
print(a.maxSubArray(nums))