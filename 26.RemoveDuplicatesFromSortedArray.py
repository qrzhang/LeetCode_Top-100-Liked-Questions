# Given a sorted array nums, remove the duplicates in-place such that each element appear only
# once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array
# in-place with O(1) extra memory.

class Solution:
    def removeDuplicates_s1(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

    def removeDuplicates_s2(self, nums):
        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[len_] = nums[i]
                len_ += 1
        return len_


nums = [1, 1, 2]
a = Solution()
a.removeDuplicates_s2(nums)
