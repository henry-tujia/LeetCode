class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self, serial=None):
        self.__size = 0
        self.__root = None
        self.__height = 0
        if serial:
            if isinstance(serial, list):
                self.construct(serial)

    # serial should be a list
    def construct(self, serial):
        self.__root = Node(serial[0])
        self.__height = 1
        self.__size = 1
        que = [[self.__root, 0], [None, 0]]
        newLevel = True
        i = 1
        while i < len(serial):
            top = que[0]
            if newLevel:
                self.__height += 1
                newLevel = False
            if top[0] is None:
                # change level
                newLevel = True
                que = que[1:]
                que.append([None, 0])
                continue
            else:
                # left node
                if top[1] == 0:
                    top[1] = 1
                    if serial[i] != '#':
                        top[0].left = Node(serial[i])
                        que.append([top[0].left, 0])
                        self.__size += 1
                # right node
                else:
                    que = que[1:]
                    if serial[i] != '#':
                        top[0].right = Node(serial[i])
                        que.append([top[0].right, 0])
                        self.__size += 1
                i += 1

    def root(self):
        return self.__root