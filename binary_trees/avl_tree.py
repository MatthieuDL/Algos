"""This is the AVL tree module (named after Adelson-Velsky and Landis)"""
class Node: # pylint: disable=R0903
    """
    A node is the smallest component in the AVL tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    """
    an AVL Tree is one of the datastructures that 
    can be used as a self balancing binary tree.
    
    https://en.wikipedia.org/wiki/AVL_tree
    
    https://www.youtube.com/watch?v=DB1HFCEdLxA
    """

    def __init__(self):
        self.root = None

    def get_height(self, node): # pylint: disable=C0116
        if not node:
            return 0
        return node.height

    def reset_height(self, node): # pylint: disable=C0116
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def balance(self, node): # pylint: disable=C0116
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, a):
        """
        Time complexity: 
            O(1)
        """
        b = a.right
        t2 = b.left

        b.left = a
        a.right = t2

        self.reset_height(a)
        self.reset_height(b)

        return b

    def rotate_right(self, a):
        """
        Time complexity: 
            O(1)
        """
        b = a.left
        t2 = b.right

        b.right = a
        a.left = t2

        self.reset_height(a)
        self.reset_height(b)

        return b

    def find_next_smallest_node(self, node):
        """
        Find the node with smallest value that is 
        larger than the value of the current node.
        """
        temp = node
        while temp.left:
            temp = temp.left
        return temp

    def search(self, val):
        """
        Time complexity: 
            O(log n) where n = number nodes in AVL tree
        """
        n = self.root
        while n is not None and n.value != val:
            if val < n.value:
                n = n.left
            else:
                n = n.right
        return n

    def insert(self, node, val):
        """
        https://www.youtube.com/watch?v=JPI-DPizQYk
        """
        if not node:
            return Node(val)
        if val < node.value:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)

        self.reset_height(node)

        bf = self.balance(node)

        if bf > 1 and val < node.left.value:
            return self.rotate_right(node)
        if bf < -1 and val > node.right.value:
            return self.rotate_left(node)
        if bf > 1 and val > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if bf < -1 and val < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def delete(self, node, val):
        """
        https://www.youtube.com/watch?v=PBkXmhiCP1M
        """
        if not node:
            return node
        if val > node.value:
            node.right = self.delete(node.right, val)
        elif val < node.value:
            node.left = self.delete(node.left, val)
        else:
            if not node.right:
                temp = node.left
                node = None
                return temp
            if not node.left:
                temp = node.right
                node = None
                return temp

            temp = self.find_next_smallest_node(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)

        self.reset_height(node)

        bf = self.balance(node)

        bf_l = self.balance(node.left)
        bf_r = self.balance(node.right)

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
