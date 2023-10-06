import argparse

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def show_order(self):
        if self.left:
            self.left.show_order()
        print(self.value)
        if self.right:
            self.right.show_order()

    def show_order_desc(self):
        if self.right:
            self.right.show_order_desc()
        print(self.value)
        if self.left:
            self.left.show_order_desc()

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return True

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Binary tree')
    parser.add_argument('-v','--value', type=int, help='value to find')
    parser.add_argument('-l','--list', type=str, help='list of values to insert, separated by comma')
    parser.add_argument('-o','--order', type=str, help='sort asc[a] or desc[d]')

    args = parser.parse_args()

    items = args.list.split(',')
    n = Node(int(items[0]))
    for i in range(1, len(items)):
        n.insert(int(items[i]))

    if args.order:
        if args.order == "a":
            n.show_order()
        
        if args.order == "d":
            n.show_order_desc()

    if args.value:
        print(n.find(args.value))