
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"TreeNode: (val: {self.val}, left: {self.left}, right: {self.right})"
    
    def __str__(self):
        return self.__repr__()
    
    def __eq__(self, other):
        
        if isinstance(other, self.__class__):
            return all([self.val==other.val, self.left==other.left, self.right==other.right])
        
        return False

class BTree:
    
    def __init__(self, arr=None):
        self.root = None if arr is None else self.btree_from_array(arr)
        
    def __repr__(self):
        return str(self.root)
    
    def __str__(self):
        return self.__repr__()
    
    def __eq__(self, other):
        
        if isinstance(other, self.__class__):
            return other.root == self.root
        
        return False
    
    @classmethod
    def btree_from_array(self, arr):
        
        n = len(arr)
        if n == 0:
            return None

        def inner(index: int = 0) -> TreeNode:

            if n <= index or arr[index] is None:
                return None

            node = TreeNode(arr[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()
