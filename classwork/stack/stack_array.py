class Stack:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)
        print(value, "pushed into stack")

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Popped element:", self.stack.pop())

    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def display(self):
        print("Stack elements:", self.stack)


st = Stack()

st.push(10)
st.push(20)
st.push(30)
st.push(40)

st.display()
st.peek()
st.pop()
st.display()
