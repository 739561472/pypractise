class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join([item[::-1] for item in s.split(' ')])