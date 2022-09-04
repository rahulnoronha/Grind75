# Definition for a binary tree node.
from collections import deque as queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def LevelOrder(root , value):
    if(root == None):
        root = TreeNode(value)
        # put in the data
        root.left =None
        root.right = None
        return root
    if(value <= root.val):
        root.left = LevelOrder(root.left, value)
    else:
        root.right = LevelOrder(root.right, value)
    return root  


def constructBst(arr, arrlen):
    if(arrlen == 0):
        return None
    root = None
    for i in range(0, arrlen):
        root = LevelOrder(root , arr[i])
    return root        


class Solution:
    def invertTree(root:TreeNode) -> TreeNode:
        if root==None:
            return root
        root.left, root.right = root.right, root.left
        Solution.invertTree(root.left)
        Solution.invertTree(root.right)
        return root
    
def levelOrderTraversal(root):
    global tree
    if (root == None):
        return
    q = queue()
    q.append(root)
    q.append(None)
    while (len(q) > 1):
        curr = q.popleft()
        if (curr == None):
           q.append(None)
           print()
        else:
            if (curr.left):
                q.append(curr.left)
            if (curr.right):
                q.append(curr.right)
            tree.append(curr.val)
            
arr = [4,2,7,1,3,6,9]
tree=[]
levelOrderTraversal(Solution.invertTree(constructBst(arr,len(arr))))
print(tree) 
 
arr = [2,1,3]
tree=[]
levelOrderTraversal(Solution.invertTree(constructBst(arr,len(arr))))
print(tree)

arr = []
tree=[]
levelOrderTraversal(Solution.invertTree(constructBst(arr,len(arr))))
print(tree)        
        
    
        