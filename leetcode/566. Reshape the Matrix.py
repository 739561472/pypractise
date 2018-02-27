class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums)*len(nums[0]):
            return nums
        else:
            l = [m for n in nums for m in n]
            return [ l[(i-1)*c:i*c] for i in range(1,r+1)]