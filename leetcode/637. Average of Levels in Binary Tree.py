# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        l = [root]
        avg , res , r = [],[],[]
        while l:
            node = l.pop()
            avg.append(node.val)
            if node.left:
                r.append(node.left)
            if node.right:
                r.append(node.right)
            if not l:
                res.append(float(sum(avg))/float(len(avg)))
                l,r,avg=r,[],[]
        return res