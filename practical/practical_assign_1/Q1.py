
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    #1. create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter value: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = new_node

    #2. display linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    #3. insert at position
    def insert(self):
        pos = int(input("Enter position: "))
        data = int(input("Enter value: "))

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    #4. find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        if slow is not None:
            print("Middle node:", slow.data)

    #5. delete node
    def delete(self):
        pos = int(input("Enter position to delete: "))

        if self.head is None:
            print("List is empty")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    #6. reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    #7. sum of consecutive nodes
    def consecutive_sum(self):
        temp = self.head

        while temp is not None and temp.next is not None:
            print(temp.data, "+", temp.next.data, "=", temp.data + temp.next.data)
            temp = temp.next


l = LinkedList()

l.create()

print("\nLinked List:")
l.display()

print("\nInsert node")
l.insert()
print("After insertion:")
l.display()

print("\nMiddle node")
l.middle()

print("\nDelete node")
l.delete()
print("After deletion:")
l.display()

print("\nReverse list")
l.reverse()
l.display()

print("\nSum of every two consecutive nodes:")
l.consecutive_sum()