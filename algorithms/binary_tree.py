class BinaryTreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        # Represents a binary root as:
        # Left node <- Actual Root -> Right Node
        return f'{self.left and self.left.key} <- {self.key} -> {self.right and self.right.key}'


def ordered_walk(root):  # Walks over the Binary Tree roots
    if not root:
        return

    # Recursive walk over the binary tree
    ordered_walk(root.left)

    print(root.key)  # Display the actual root

    ordered_walk(root.right)

def ordered_search(root, key):  # Search for a key on the Binary Tree
    if root is None:
        return None

    if root.key == key: # Checks if the desired key is on tree root
        return root

    if root.key < key: # Checks if the desired keys is greater than root value
        return ordered_search(root.right, key)

    if root.key > key: # Checks if the desired key is less than root value
        return ordered_search(root.left, key)


# Represents a simple binary tree
root = BinaryTreeNode(3)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(1)

print('Simple tree')
print(root)
print()

# Represents a more complex binary tree
c_root = BinaryTreeNode(40)

c_root.left = BinaryTreeNode(20)
c_root.right = BinaryTreeNode(60)

c_root.right.left = BinaryTreeNode(50)
c_root.right.right = BinaryTreeNode(70)
c_root.left.left = BinaryTreeNode(10)
c_root.left.right = BinaryTreeNode(30)

print('Example complex tree')
print(c_root)
print(c_root.left)
print(c_root.right)
print()


print('Complex tree walk: ')
ordered_walk(c_root)
print()

value = 30

print(f'Search for {value} on complex tree: ')

result = ordered_search(c_root, value)

if result:
    print(f'{result}')
else:
    print(f'The value {value} does not exist on this tree')

