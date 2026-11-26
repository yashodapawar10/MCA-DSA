
# Sort Stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def sort(self):
        self.stack.sort()
        print("Sorted Stack:", self.stack)

    def display(self):
        print("Stack:", self.stack)


st = Stack()
st.push(40)
st.push(10)
st.push(30)
st.push(20)

st.display()
st.sort()
st.display()
