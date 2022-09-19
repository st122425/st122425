#how do we start here
#create a class called Node
class Node(object):  #object is the primitive class, so I inherit
    pass

    #left``
    #right
    #key
    #when you first create the Node, this guy is the root node
    def __init__(self, key):
        self.left  = None
        self.right = None
        self.key = key  #this is actually the root node
        #why you don't write like this
        #self.root = key
        
    #def insert
    def insert(self, key):
        #if we already have a root node,
        if(self.key):
            #then check left and right
            #cond1:  if less than: go left, self.key is parent
            if(key < self.key):
                #cond1.1  if the left is NIL, yay! fill it!
                if(self.left == None):
                    self.left = Node(key)
                #cond1.2  if the left is NOT NIL...oh no...
                else:
                    self.left.insert(key)
            
            #cond2:  if greater than: go right
            elif(key >= self.key):
                #cond1.2  if the right is NIL, yay! fill it!
                if(self.right == None):
                    self.right = Node(key)
                #cond1.2  if the right is NOT NIL...consider right as the parent...
                else:
                    self.right.insert(key)
            
            
        #if we don't have the root node
        else:
            #this key is the root node
            self.key = key
    
    #def printTree
    def printT(self):        
        #if left is still available print left
        if (self.left):
            self.left.printT()
        print(self.key)
        if (self.right):
            self.right.printT()

    
    #def delete
    def deleteNode(self, z):
        if self.key is None:
            print("There is no BST")
            return
        #if z is less than root node   
        if z < self.key:
            if self.left:
                self.left = self.left.deleteNode(z)
            else:
                print("there is given node")
        elif z > self.key:
            if self.right:
                self.right = self.right.deleteNode(z)
            else:
                print("there is no given node")
        else:
            # if left is none, right will be the key
            if self.left is None:
                temp = self.right
                self = None
                return temp
            # if right in none, left will be the key
            if self.right is None:
                temp = self.left
                self = None
                return temp
            # if left and right is not none, right will be the key
            Node = self.right
            while Node.left:
                Node = Node.left
            self.key = Node.key
            self.right = self.right.deleteNode(Node.key)
        return self

    
    #def minimum
    

    #def successor
    
#try our class
root = Node(10)
root.insert(11)
root.insert(5)
root.insert(3)
root.printT()

root.deleteNode(5)
print("after deletion")
root.printT()