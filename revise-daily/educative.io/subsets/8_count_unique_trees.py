# Count of Structurally Unique Binary Search Trees (hard) #
# Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.

# Input: 2
# Output: 2
# Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_trees(n):
    if n <= 1:
        return 1
    count = 0
    for i in range(1, n + 1):
        # making 'i' root of the tree
        countOfLeftSubtrees = count_trees(i - 1)
        countOfRightSubtrees = count_trees(n - i)
        count += (countOfLeftSubtrees * countOfRightSubtrees)

    return count


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
