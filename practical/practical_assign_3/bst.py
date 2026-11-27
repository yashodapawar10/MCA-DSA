# BST for Online Examination Result Management

class Node:
    def __init__(self, score):
        self.score = score
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    # Insert node
    def insertnode(self, score):
        if self.root is None:
            self.root = Node(score)
            self.count += 1
        else:
            self._insert(self.root, score)

    def _insert(self, root, score):
        if score < root.score:
            if root.left is None:
                root.left = Node(score)
                self.count += 1
            else:
                self._insert(root.left, score)

        elif score > root.score:
            if root.right is None:
                root.right = Node(score)
                self.count += 1
            else:
                self._insert(root.right, score)

    # Display in ascending order
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.score, end=" ")
            self.inorder(root.right)

    # Find lowest score
    def findmin(self):
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp.score

    # Find highest score
    def findmax(self):
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp.score

    # Count scores above 50
    def countabove50(self, root):
        if root is None:
            return 0

        count = 1 if root.score > 50 else 0

        return (count +
                self.countabove50(root.left) +
                self.countabove50(root.right))

    # Search a score
    def search(self, root, key):
        if root is None:
            return False

        if root.score == key:
            return True

        if key < root.score:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Calculate total scores
    def total(self, root):
        if root is None:
            return 0

        return (root.score +
                self.total(root.left) +
                self.total(root.right))

    # Calculate average
    def average(self):
        return self.total(self.root) / self.count


# Create BST
b1 = BST()

# Insert examination scores
scores = [45, 78, 32, 89, 56, 92,
          67, 34, 85, 73, 61, 98]

for score in scores:
    b1.insertnode(score)

# Display scores in ascending order
print("Scores in ascending order:")
b1.inorder(b1.root)
print()

# Find lowest and highest scores
print("Lowest score:", b1.findmin())
print("Highest score:", b1.findmax())

# Count students scoring above 50
print("Students scoring above 50:",
      b1.countabove50(b1.root))

# Search for a particular score
key = 78

if b1.search(b1.root, key):
    print("Score", key, "found in BST")
else:
    print("Score", key, "not found in BST")

# Find average score
print("Average score:", round(b1.average(), 2))