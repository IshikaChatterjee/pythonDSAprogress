# Implementing Python Tree Data Structure
# Creating a class for node object
class Node(object):
    # Initializing to None
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

# Inserting a node in Binary search tree
def insertion(val):
    # Condition if this is a first node then it will be considered as a root
    if(root.data==None):
        print(val," Inserted as root")
        root.data=val
    # Else part will be executed for all the other insertions
    else:
        # Pointer to move around tree to search for a place of new node
        p=root
        
        # Creating a new node and writing a value in the data part
        n = Node()
        n.data=val
        
        # Iterating to search for an appropriate place of new node
        while(1):
            # if val is less than the current node p indicates that new node will be inserted on left subtree
            if(val<p.data):
                if(p.left==None):
                    print(val," Inserted on left of ",p.data)
                    p.left=n
                    break
                else:
                    p=p.left
            # if val is greater than the current node p indicates that new node will be inserted on right subtree
            else:
                if(p.right==None):
                    print(val," Inserted on right of",p.data)
                    p.right=n
                    break
                else:
                    p=p.right

root = Node()  
insertion(10)
insertion(5)
insertion(20)
insertion(30)
insertion(25)
insertion(2)
'''
           10
          /  \
         5   20
        /      \
       2       30
              /
             25
'''
