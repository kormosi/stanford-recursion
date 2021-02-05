# 5. Write a recursive function that, given a pointer to the root of a binary
# search tree, prints out the elements in that tree in sorted order.

class BST():
    def __init__(self, value, left_child, right_child):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


bst = BST(8, BST(3, BST(1, None, None), BST(6, BST(4, None, None,), BST(7, None, None))), BST(10, None, BST(14, BST(13, None, None), None)))

def print_elements_in_order(root):
    if root.left_child:
        print_elements_in_order(root.left_child)
    print(root.value)
    if root.right_child:
        print_elements_in_order(root.right_child)


print_elements_in_order(bst)
