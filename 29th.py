class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def create(self, values):
        for value in values:
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return

            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node:", slow.data)

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next and temp.next.data != data:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
        else:
            print("Value not found")

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def consecutive_sums(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp = temp.next

        print()


linked_list = SinglyLinkedList()

print("1. Create Linked List")
linked_list.create([10, 20, 30, 40, 50])
print("Linked List created successfully.")

print("\n2. Traverse")
linked_list.traverse()

print("\n3. Insert 25 at position 3")
linked_list.insert_at_position(25, 3)
linked_list.traverse()

print("\n4. Middle Node")
linked_list.middle()

print("\n5. Delete 25")
linked_list.delete(25)
linked_list.traverse()

print("\n6. Reverse List")
linked_list.reverse()
linked_list.traverse()

print("\n7. Sum of consecutive nodes")
linked_list.consecutive_sums()