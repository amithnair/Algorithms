# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    result = True
    
    def isBalanced(self, A):
        self.find_depth(A)
        return self.result
        
    def find_depth(self, A):
        
        left_depth = 1
        right_depth = 1
        
        
        if(A == None):
            return -1
        if(A.left == A.right == None):
            return 0
        
        '''if isleft:
            if A.left == None:
                return 1
        else:
            if A.right == None:
                return 1'''
        
        
        
        left_d = self.find_depth(A.left) + 1
        right_d = self.find_depth(A.right) + 1
        
        if abs(left_depth - right_depth) > 1:
            self.result = False
        
        return max(left_depth , right_depth) 