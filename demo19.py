
class node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.front is None:
            self.front = self.rear = new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next:
            if new_node.priority < temp.next.priority:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        if new_node.next is None:
            self.rear = new_node

    def display(self):
        if self.front is None:
            print("Priority Queue is empty")
            return

        temp = self.front

        while temp:
            print(temp.data, "Priority:", temp.priority)
            temp = temp.next


pq = PriorityQueue()

pq.enqueue(node(10, 2))
pq.enqueue(node(20, 1))
pq.enqueue(node(30, 3))
pq.enqueue(node(40, 2))
pq.enqueue(node(50, 4))

print("Priority Queue:")
pq.display()
