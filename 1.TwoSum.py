class Solution:
    def twoSum(self, nums, target):
        """Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        Parameters
        ----------
            nums: `List[int]`
            target: int
        Returns
        -------
            Index of two numbers.
        """

        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in h:
                return [h[n], i]
            h[num] = i
        return 'No two sum solution'



a = Solution()
print(a.twoSum([2, 7, 11, 15], 9))
print(a.twoSum([], 3))