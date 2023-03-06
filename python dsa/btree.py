### preorder traversal of binary tree

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")   ### Time complexity -------> O(1)  Space complexity ------> O(1)
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode): ### ------> O(1)
    if not rootNode:             ### ------> O(1)
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)  ### ------> O(n/2)
    preOrderTraversal(rootNode.rightChild) ### ------> O(n/2) ---> O(n)
    

preOrderTraversal(newBT)
