
# Circular Queue using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class CQueue:
    def __init__(self):
        self.front = self.rear = None

    # Enqueue - Insert element
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

        self.rear.next = self.front

    # Dequeue - Delete element
    def dequeue(self):
        if self.front:
            temp = self.front

            print("Deleted element:", temp.data)

            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.rear.next = self.front

            temp = None

        else:
            print("Queue is empty")

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.front:
                break

        print()


# Main program
que = CQueue()

que.enqueue(Node(15))
que.enqueue(Node(67))
que.enqueue(Node(55))
que.enqueue(Node(100))
que.enqueue(Node(88))

que.display()

que.dequeue()
que.display()

que.dequeue()
que.dequeue()
que.dequeue()

que.display()

que.dequeue()

que.enqueue(Node(23))
que.enqueue(Node(98))

que.display()
