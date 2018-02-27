class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = '{0:b}'.format(n)
        for i in range(len(s)-1):
            if s[i] == s[i+1] :
                return False
        return True