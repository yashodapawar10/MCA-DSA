
# Find Maximum Element in Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def maximum(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Maximum element:", max(self.stack))

    def display(self):
        print("Stack:", self.stack)


st = Stack()
st.push(25)
st.push(10)
st.push(50)
st.push(35)
st.push(15)

st.display()
st.maximum()
