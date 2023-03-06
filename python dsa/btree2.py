### Write the preorder traversal for the given binary tree 
### 15 10 6 14 25 20 60

class BTREE:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

def insert(root,newValue):
    
    if root is None:
        root = BTREE(newValue)
        return root
    
    
    if newValue< root.data:
        root.leftchild = insert(root.leftchild, newValue)

    else:

        root.rightchild = insert(root.rightchild, newValue)
    
    return root

def preorder(root):
    
    if root == None:
        return
    print(root.data)

    preorder(root.leftchild)

    preorder(root.rightchild)


root = insert(None, 15)
insert(root, 10)
insert(root, 6)
insert(root, 14)
insert(root, 25)
insert(root, 20)
insert(root, 60)

print("Preorder traversal for the btree : ")
preorder(root)