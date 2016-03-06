# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class IterationInorderTreeTraversal:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []
        ls = []
        
        while (len(stack) != 0 or A != None):
            if(A != None):
                stack.append(A)
                A = A.left
            else:
                A = stack.pop()
                ls.append(A.val)
                A = A.right
        return ls
            