
# Linear Queue using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LQueue:
    def __init__(self):
        self.front = self.rear = None

    # Enqueue - Insert element
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    # Dequeue - Delete element
    def dequeue(self):
        if self.front:
            temp = self.front
            print("Deleted element:", temp.data)

            self.front = self.front.next

            if self.front == None:
                self.rear = None
                print("Now queue is empty")

            temp = None

        else:
            print("Queue is empty")

    # Display queue
    def print(self):
        temp = self.front

        if temp == None:
            print("Queue is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
que = LQueue()

que.enqueue(Node(15))
que.enqueue(Node(67))
que.enqueue(Node(55))
que.enqueue(Node(100))
que.enqueue(Node(88))

que.print()

que.dequeue()
que.print()

que.dequeue()
que.dequeue()
que.dequeue()

que.print()

que.dequeue()

que.enqueue(Node(23))
que.enqueue(Node(98))

que.print()
