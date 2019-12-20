# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == value:
            return
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value >= self.value:
            if self.right:
                # self.right = value
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
                return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else: 
                return False 
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def get_min(self):
        if self.left:
            return self.left.get_min()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            if node.left:
                self.in_order_print(node.left)
            print(node.value)
            if node.right:
                self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        bft_node = BinarySearchTree(node)
        queue.enqueue(bft_node.value)
        while queue.len() > 0:
            cur_node = queue.dequeue()
            print(cur_node.value)
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        dft_node = BinarySearchTree(node)
        stack.push(dft_node.value)
        while stack.len() > 0:
            cur_node = stack.pop()
            print(cur_node.value)
            if cur_node.left:
                stack.push(cur_node.left)
            if cur_node.right:
                stack.push(cur_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
