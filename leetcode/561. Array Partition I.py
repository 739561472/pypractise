class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort()
        for i in range(int(len(nums) / 2)):
            sum += nums[2 * i]
        return sum
