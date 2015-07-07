class BST:

    # Checks if a binary tree is a binary search tree.
    # root - node with `left`, `right` and `value` properties

    class TreeNode:
        def __init__(self, value, left_child=None, right_child=None):
            self.value = value
            self.left = left_child
            self.right = right_child

        @staticmethod
        def create_node(values, index):
            if index >= len(values) or values[index] == 0:
                return None

            root = BST.TreeNode(values[index])
            root.left = BST.TreeNode.create_node(values, index * 2 + 1)
            root.right = BST.TreeNode.create_node(values, index * 2 + 2)

            return root

        def size(self):
            result = 1
            if self.left:
                result += self.left.size()
            if self.right:
                result += self.right.size()

            return result

        def left_root_right(self, result):
            if self.left:
                self.left.left_root_right(result)

            result.append(self.value)

            if self.right:
                self.right.left_root_right(result)

    @staticmethod
    def isBST(root):
        values = []
        root.left_root_right(values)

        for index in range(len(values) - 1):
            if values[index] > values[index + 1]:
                return False

        return True


def main():
    N = int(input())
    line = input()
    l = line.split()
    result = []

    for number in l:
        result.append(int(number))

    root = BST.TreeNode.create_node(result, 0)
    if BST.isBST(root):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
