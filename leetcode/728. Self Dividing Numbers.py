class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l=[]
        for m in range(left, right+1):
            n=0
            if m < 10:
                l.append(m)
            elif '0' in str(m):
                pass
            else:
                for i in str(m):
                    if m % int(i) == 0:
                        n+=1
                if n == len(str(m)):
                    l.append(m)
        return l