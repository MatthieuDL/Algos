"""This module contains implementation of a complete binary tree"""

class Node: # pylint: disable=C0115, disable=R0903
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

    def has_left(self):
        if self.left is not None:
            return True
        return False

    def has_right(self):
        if self.right is not None:
            return True
        return False


class CompleteBinaryTree:
    """
    A complete binary tree is a binary tree 
    in which all levels are filled except the bottom,
    which is filled from the left.
    
    https://www.programiz.com/dsa/complete-binary-tree    
    """

    @staticmethod
    def generate_from_list(input_list):
        """Turns a list into a complete binary tree"""
        def _generate_node(index):
            if index < len(input_list):
                node = Node(input_list[index])
                node.left = _generate_node(2 * index + 1)
                node.right = _generate_node(2 * index + 2)
                return node
            return None

        return _generate_node(0)

    def __init__(self, root: Node = None, input_list: list = None):
        if list is not None:
            self.root = self.generate_from_list(input_list)
        else:
            self.root = root

    def __str__(self):
        if not self.root:
            return '<empty tree>'

        def _traverse(node):
            if not node:
                return []
            left = _traverse(node.left)
            right = _traverse(node.right)
            return [node.item] + left + right

        return ' '.join(map(str, _traverse(self.root)))

    def get_root(self):
        return self.root

    def set_root(self, root: Node):
        self.root = root


    #def count_nodes(self):
    #    root = self.root
    #    if root is None:
    #        return 0
    #    return (1 + count_nodes(root.left) + count_nodes(root.right))

if __name__ == "__main__":
    print(CompleteBinaryTree(input_list=[1,2,3,5]))