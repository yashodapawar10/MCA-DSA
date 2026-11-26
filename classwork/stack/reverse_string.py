class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

st = Stack()

string = input("Enter a string: ")

for ch in string:
    st.push(ch)

reverse = ""

while len(st.stack) > 0:
    reverse += st.pop()

print("Original string:", string)
print("Reversed string:", reverse)
