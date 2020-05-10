from time import time


class Timer(object):
    def __init__(self, description):
        self.description = description

    def __enter__(self):
        self.start = time()

    def __exit__(self, type, value, traceback):
        self.end = time()
        # print(f"{self.description}: {self.end - self.start}")

# Overriding __iter__ in set


class CustomizeList(list):

    def __iter__(self):
        for i in super(CustomizeList, self).__iter__():
            yield i


with Timer("Using CustomizeList") as e:
    a = CustomizeList(range(10))
    for i in a:
        pass

with Timer("Using InBuilt list") as e:
    a = list(range(10))
    for i in a:
        pass

# Overriding __iter__ in set


class IterableSet(set):
    def __iter__(self):
        for _item in super(IterableSet, self).__iter__():
            yield _item


iterable_set = IterableSet([1, 2, 3, 4])

with Timer("On custom iterable set") as e:
    for item in iterable_set:
        pass


primitive_set = {1, 2, 3, 4}
with Timer("On primitive iterable set") as e:
    for item in primitive_set.__iter__():
        pass


# Iterable class on Tree
import enum
from typing import  Any


class TreeIteratorModes(enum.Enum):
    BFS = ("BFS", "Breadth First Search")
    DFS = ("DFS", "Depth First Search")


class BFSTraversal:

    @staticmethod
    def print_level_order(height: int, root):
        items = []
        for i in range(1, height + 1):
            res = BFSTraversal.print_given_level(root, i)
            if res is not None:
                items.extend(res)

        for item in items:
            yield (item)

    @staticmethod
    def print_given_level(root, level: int):
        a = []
        if root is None:
            return
        if level == 1:
            a.append(root.value)
        elif level > 1:
            a.extend(BFSTraversal.print_given_level(root.left, level - 1))
            a.extend(BFSTraversal.print_given_level(root.right, level - 1))
        return a


class AbstractTree:

    def __init__(self):
        self.left = None
        self.right = None
        self.iterable_mode = None

    def __iter__(self):
        if self.iterable_mode == TreeIteratorModes.BFS.value[0]:
            return self.iterate_using_bfs(self)
        if self.iterable_mode == TreeIteratorModes.DFS.value[0]:
            yield self.iterate_using_dfs()

    def __call__(self, *args, **kwargs):
        self.iterable_mode = kwargs["mode"]
        return self

    @staticmethod
    def get_height(node) -> int:
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = AbstractTree.get_height(node.left)
            rheight = AbstractTree.get_height(node.right)

            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    @staticmethod
    def iterate_using_bfs(node):
        _height: int = AbstractTree.get_height(node)
        return BFSTraversal.print_level_order(_height, node)

    def iterate_using_dfs(self):
        yield 0


class TreeNode(AbstractTree):

    def __init__(self, value: Any, left: AbstractTree = None, right: AbstractTree = None):
        super(TreeNode, self).__init__()
        self.value = value
        self.left = left
        self.right = right
        self.iterable_mode = None

    def __iter__(self):
        return super(TreeNode, self).__iter__()


root = TreeNode(1)

root_left = TreeNode(2)
root_right = TreeNode(3)

root.left = root_left
root.right = root_right

root_left_left = TreeNode(4)
root_left_right = TreeNode(5)

root_left.left = root_left_left
root_left.right = root_left_right

root_right_left = TreeNode(6)
root_right_right = TreeNode(7)

root_right.left = root_right_left
root_right.right = root_right_right


for item in root(mode=TreeIteratorModes.BFS.value[0]):
    print (type(item))
    print (item)