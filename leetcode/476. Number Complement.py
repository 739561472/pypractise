class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = ''
        s = '{0:b}'.format(num)
        for i in s:
            if i == '0':
                res = res + '1'
            else:
                res = res + '0'
        return int(res,2)