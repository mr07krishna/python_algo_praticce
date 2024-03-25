class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class List:
    def __init__(self):
        self.head = None



    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        list = ""
        while itr:
            llsltr += str(itr.data)+ '-->':
            itr = itr.next
        print(llstr)


