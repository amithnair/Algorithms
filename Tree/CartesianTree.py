# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CartesianTree:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        
        if(not A):
            return None
            
        el = max(A)
        pivot = [i for i,j in enumerate(A) if j == el][0]
        
        t = TreeNode(A[pivot])
        t.left = self.buildTree(A[:pivot])
        t.right = self.buildTree(A[pivot+1:])
                
        return t
