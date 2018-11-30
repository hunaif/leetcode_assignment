# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from sys import maxint
# minimum_int = -maxint - 2

class Solution:

    def __init__(self):
        self.sum = -1000 #Not a good initialization

    def maxSum(self,node):
        if node == None:
            return 0

        left_sum = self.maxSum(node.left)
        right_sum = self.maxSum(node.right)

        #Should include either left and current node
        ## Or include right and current node
        ## Or exclude both children
        max_child = max(left_sum , right_sum)
        max_including_current_node_with_atmost_one_child = max(max_child + node.val , node.val)

        #Incase max path lies through current node as root
        #ie consider left and right child through current node
        max_sum = max(max_including_current_node_with_atmost_one_child, node.val + left_sum + right_sum)
        self.sum = max(self.sum,max_sum)

        return max_including_current_node_with_atmost_one_child

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum(root)
        return self.sum