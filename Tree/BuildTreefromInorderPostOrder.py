class BuildTreefromInorderPostOrder:
    # @param inorder : list of integers denoting inorder traversal
    # @param postorder : list of integers denoting postorder traversal
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        
        if not postorder or not inorder:
            return None
            
        #print 'inorder' + ' '.join([str(x) for x in inorder])
        #print 'postorder' + ' '.join([str(x) for x in postorder])
        
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        
        #print root.val
        #print 'XXXXXXXXX'
        left = inorder[:idx]
        right = inorder[idx+1:]
        postorder.pop(-1)
        m  = len(left)
        
        root.left = self.buildTree(left, postorder[:m])
        root.right = self.buildTree(right, postorder[m:])
        
        return root