class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        st = []
        for i in range(len(findNums)):
            for n in nums[nums.index(findNums[i])+1:]:
                if findNums[i] < n:
                    st.append(n)
                    break
            if len(st)-1 < i:
                st.append(-1)
        return st