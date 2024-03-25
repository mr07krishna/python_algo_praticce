class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class S11:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("sing Link list is empty")

        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next



n1 = Node(5)
s11 = S11()
s11.head = n1
n2 = Node(10)
n1.next = n2


