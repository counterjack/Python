

class Node:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class BST:

    def __init__(self, root: Node) -> None:
        self.root = root

    def add_item(self, node: Node, data: int) -> Node:
        """[This is used to add a new item to the BST]

        :return: [update node after adding a new item]
        :rtype: [Node]
        """

        # base condition
        if not node:
            return Node(data)

        # If the data is lesser to root then insert in the left subtree
        if data < node.data:
            node.left = self.add_item(node.left, data)

        # If the data is greater to root then insert in the right subtree
        else:
            node.right = self.add_item(node.right, data)
        return node

    def _remove_item(self, node: Node, item: int):
        if item == node.data:
            pass

        if item < node.data:
            node.left = self._remove_item(node.left, item)
        else:
            node.right = self._remove_item(node.right, item)

    def remove_item(self, node: Node, item: int):
        self._remove_item(self.root, item)

    def _inorder(self, node: Node) -> None:
        if node is None:
            return

        self._inorder(node.left)
        print (node.data)
        self._inorder(node.right)

    def inorder(self) -> None:
        """[Traverse in in order fashion and print the items]
        """
        print ("\nPrinting in InOrder Fashion \n")
        self._inorder(self.root)

    def _post_order(self, node: Node) -> None:
        if node is None:
            return

        self._post_order(node.left)
        self._post_order(node.right)
        print (node.data)

    def post_order(self):
        """[Traverse in post order fashion and print the items]
        """
        print ("\nPrinting in PostOrder Fashion \n")
        self._post_order(self.root)

    def _pre_order(self, node: Node)  -> None:
        if node is None:
            return

        print (node.data)
        self._pre_order(node.left)
        self._pre_order(node.right)

    def pre_order(self):
        """[Traverse in pre order fashion and print the items]
        """
        print ("\nPrinting in PreOrder Fashion \n")
        self._pre_order(self.root)


if __name__ == "__main__":
    root_node = Node(data=10)
    bst = BST(root=root_node)

    bst.add_item(bst.root, 9)
    bst.add_item(bst.root, 7)
    bst.add_item(bst.root, 8)
    bst.add_item(bst.root, 12)
    bst.add_item(bst.root, 3)
    bst.add_item(bst.root, 11)

    bst.inorder()
    bst.post_order()
    bst.pre_order()