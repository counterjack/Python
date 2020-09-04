


class Node():

    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def add(self, data):
        """[Will add the new node at the end of the linked list]

        Arguments:
            data

        Returns:
            [DoublyLinkedList] -- [Returns new node]
        """
        root_copy= self
        while (root_copy.right):
            root_copy = root_copy.right
        new_node = DoublyLinkedList(data, root_copy, None)
        root_copy.right = new_node
        return new_node

    @staticmethod
    def preorder(root_node):
        if (root_node == None):
            return

        Node.preorder(root_node.left)
        print (root_node.data)
        Node.preorder(root_node.right)

    @staticmethod
    def _print_dll(root_node) -> None:
        """
        Prints the doubly linked list
        """
        new_object = root_node
        iterate_further = True
        while (new_object.right):
            print (new_object.data)
            iterate_further = new_object.right != None
            new_object = new_object.right
        print (new_object.data)

def bst_to_dll(bst: Node, new_node: Node, prev=None) -> Node:
    """
    returns the updated new_node after converting bst to dll
    """

    if bst is None:
        return

    bst_to_dll(bst.left, new_node)

    # print (bst.data)
    if (not prev):
        # Case when it's left leaf in left subtree
        new_node = bst

    else:
        new_node.right = prev
        prev.left = new_node
    prev = new_node
    # print (new_node.data)


    bst_to_dll(bst.right, new_node)
    # return new_node



if __name__ == "__main__":

    bst = Node(10)
    bst.left = Node(data=8)
    # print (bst.left.data)
    bst.right = Node(data=12)
    # print (bst.right.data)
    bst.left.left = Node(data=6)
    # print (bst.left.left.data)
    bst.left.right = Node(data=7)
    # print (bst.left.right.data)
    # Node.preorder(bst)


    dll = Node()
    # dll.right = Node(12)
    # dll.right.left = dll
    # dll.right.right = Node(13)
    # dll.right.right.left = dll.right
    # dll.

    dll = bst_to_dll(bst, dll)
    Node._print_dll(dll)









