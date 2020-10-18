

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree 
    '''def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False
    '''
    def search(self, e):
        return self.searchHelper(self.root, e) # Start from the root

    def searchHelper(self, current, e): # Search from the current subtree
        if current == None:
            return False
        elif e < current.element:
            return self.searchHelper(current.left, e)
        elif e == current.element:
            return True
        else:
            return self.searchHelper(current.right, e)
    
    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully 
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size
    
    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree 
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root 
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element 
    def path(self, e):
        list = []
        current = self.root # Start from the root

        while current != None:
            list.append(current) # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element: 
                parent = current
                current = current.right
            else:
                break # Element is in the tree pointed by current

        if current == None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left     

        self.size -= 1
        return True # Element deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None

# BEGIN SUBMISSION TO REVEL
class MyBST(BST):
    def __init__(self):
        BST.__init__(self)
        
    def hasSameShape(self, tree):
        return self.isSameShape(self.root, tree.root)
    
    def isSameShape(self, r1, r2):
        #if r1 and r2 are both empty, they are the same shape
        if r1 == None and r2 == None:
            return True
        #if r1 or r2 is empty and the other is not, they are not the same shape
        elif (r1 == None or r2 == None):
            return False
        #if r1 and r2 both are a single node, they are equal
        elif (r1.left == None and r2.left == None) and (r1.right == None and r2.right == None):
            return True
        
        #if not, call recursivley on the next two nodes, return the truth of those calls.
        else:
            leftstatus = self.isNodesSame(r1.left,r2.left) 
            rightstatus =self.isNodesSame(r1.right,r2.right)
            if leftstatus and rightstatus:
                truthR = self.isSameShape(r1.left, r2.left)
                truthL = self.isSameShape(r1.right,r2.right)
            else:
                return False
                if truthR and truthL:
                    return True
                else:
                    return False
    
    def isNodesSame(self,n1,n2):
        if (n1 != None and n2 != None) or (n1 == None and n2 == None):
            return True
        else:
            return False
    
# END SUBMISSION TO REVEL

def main():
    # Test one tree empty, the other not
    print("Testing one tree empty, the other not")
    tree1 = MyBST()
    tree1.insert(10)
    tree1.insert(15)
    tree1.insert(20)
    tree2 = MyBST()
    ans = tree1.hasSameShape(tree2)
    print("hasSameShape returns", ans)
    if ans:
        print("Incorrect.  They are not the same shape")
    else:
        print("Correct.  They are not the same shape.")
    print()

    # Test both trees empty
    print("Test both trees empty")
    tree1 = MyBST()
    tree2 = MyBST()
    ans = tree1.hasSameShape(tree2)
    print("hasSameShape returns", ans)
    if ans:
        print("Correct.  They are the same shape")
    else:
        print("Incorrect.  They are the same shape.")
    print()

    # Test both trees have one node.
    print("Test both trees have one node but different values")
    tree1 = MyBST()
    tree1.insert(10)
    tree2 = MyBST()
    tree2.insert(30)
    ans = tree1.hasSameShape(tree2)
    print("hasSameShape returns", ans)
    if ans:
        print("Correct.  They are the same shape")
    else:
        print("Incorrect.  They are the same shape.")
    print()

    # Test both trees have a root with two children and no other nodes.
    print("Test both trees have a root with two children and no other nodes")
    tree1 = MyBST()
    nums1 = [5, 10, 3]
    for num in nums1:
        tree1.insert(num)
    tree2 = MyBST()
    nums2 = [50, 100, 30]
    for num in nums2:
        tree2.insert(num)
    ans = tree1.hasSameShape(tree2)
    print("hasSameShape returns", ans)
    if ans:
        print("Correct.  They are the same shape")
    else:
        print("Incorrect.  They are the same shape.")
    print()

    # Test tree1 has left child, tree2 has right child.
    print("Test tree1 has left child, tree2 has right child.")
    tree1 = MyBST()
    nums1 = [5, 10]
    for num in nums1:
        tree1.insert(num)
    tree2 = MyBST()
    nums2 = [10, 5]
    for num in nums2:
        tree2.insert(num)
    ans = tree1.hasSameShape(tree2)
    print("hasSameShape returns", ans)
    if ans:
        print("Incorrect.  They are not the same shape")
    else:
        print("Correct.  They are not the same shape.")
    print()

    # Test tree1 has right child, tree2 has left child.
    print("Test tree1 has left child, tree2 has right child.")
    tree1 = MyBST()
    nums1 = [10, 5]
    for num in nums1:
        tree1.insert(num)
    tree2 = MyBST()
    nums2 = [5, 10]
    for num in nums2:
        tree2.insert(num)
    ans = tree1.hasSameShape(tree2)
    print("hasSameShape returns", ans)
    if ans:
        print("Incorrect.  They are not the same shape")
    else:
        print("Correct.  They are not the same shape.")
    print()

    # Test larger problem where tree1 and tree2 have same shape.
    print("Test larger problem where tree1 and tree2 have same shape.")
    tree1 = MyBST()
    nums1 = [50, 20, 5, 70, 60, 75, 72, 80, 73]
    for num in nums1:
        tree1.insert(num)
    tree2 = MyBST()
    nums2 = [500, 200, 700, 600, 750, 800, 720, 730, 50]
    for num in nums2:
        tree2.insert(num)
    ans = tree1.hasSameShape(tree2)
    print("hasSameShape returns", ans)
    if ans:
        print("Correct.  They are the same shape")
    else:
        print("Incorrect.  They are the same shape.")
    print()

    # Test larger problem where tree1 and tree2 have same shape.
    print("Test larger problem where tree1 and tree2 are not the same shape.")
    tree1 = MyBST()
    nums1 = [50, 20, 5, 75, 60, 70, 72, 80, 73]
    for num in nums1:
        tree1.insert(num)
    tree2 = MyBST()
    nums2 = [500, 200, 700, 600, 750, 800, 720, 730, 50]
    for num in nums2:
        tree2.insert(num)
    ans = tree1.hasSameShape(tree2)
    print("hasSameShape returns", ans)
    if ans:
        print("Incorrect.  They are not the same shape")
    else:
        print("Correct.  They are not the same shape.")
    print()

    




main()