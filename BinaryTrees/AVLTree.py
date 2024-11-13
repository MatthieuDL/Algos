# AVL Tree is one of the datastructures that can be used as a self balancing binary tree
# https://www.youtube.com/watch?v=DB1HFCEdLxA

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_left(self, a):
    #O(1)
        b = a.right
        t2 = b.left

        b.left = a
        a.right = t2
        
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))
        b.height = 1 + max(self.get_height(b.left), self.get_height(b.right))

        return b

    def rotate_right(self, a):
    #O(1)
        b = a.left
        t2 = b.right

        b.right = a
        a.left = t2

        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))
        b.height = 1 + max(self.get_height(b.left), self.get_height(b.right))

        return b

    def find_smallest_node(self, node):
        temp = node
        while temp.left:
            temp = temp.left
        return temp

    def search(self, val):
    # O(log n) where n = number nodes in AVL tree
        n = self.root
        while n is not None or n.value != val:
            if val < n.value:
                n = n.left
            else:
                n = n.right
        return n
    
    def insert(self, node, val):
    #https://www.youtube.com/watch?v=JPI-DPizQYk
        if not node:
            return Node(val)
        elif val < node.value:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        bf = self.get_height(node.left) - self.get_height(node.right)

        if bf > 1 and val < node.left.value:
            return self.rotate_right(node)
        elif bf < -1 and val > node.right.value:
            return self.rotate_left(node)
        elif bf > 1 and val > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        elif bf < -1 and val < node.rigt.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def delete(self, node, val):
    # https://www.youtube.com/watch?v=PBkXmhiCP1M
        if not node:
            return node
        elif val > node.value:
            node.right = self.delete(node.right, val)
        elif val < node.value:
            node.left = self.delete(node.left, val)
        else:
            if not node.right:
                temp = node.left
                node = None
                return temp
            elif not node.left:
                temp = node.right
                node = None
                return temp
            
            # find inorder successor (node with smallest value that is larger than the value of this node)
            temp = self.find_smallest_node(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        bf = self.height(node.left) - self.height(node.right)

        bf_l = self.height(node.left.left) - self.height(node.left.right)
        bf_r = self.height(node.right.left) - self.height(node.right.right)

        if bf > 1 and bf_l >= 0:
            return self.rotate_right(node)
        if bf < -1 and bf_r <= 0:
            return self.rotate_left(node)
        if bf > 1 and bf_l < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if bf < -1 and bf_r > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
            
        return node

        

        


        


