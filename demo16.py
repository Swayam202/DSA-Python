# write a function to delete first and last node in SLL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_first(self):
        if self.head is None:
            return

        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


l = LinkedList()

l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)

print("Original list:")
l.display()

l.delete_first()

print("After deleting first node:")
l.display()

l.delete_last()

print("After deleting last node:")
l.display()