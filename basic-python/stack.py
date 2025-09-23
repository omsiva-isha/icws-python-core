class Stack:
    gitem=[]
    def __init__(self):
        self.items = [ ]
        print("calling intially")
        
    def push(self, item):
        a=0
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack by ranjana")
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0

st=Stack()
st1=Stack()
st.gitem.append("22")
st1.gitem.append("33")
st1.push(66)
st.push(88)
st.push(77)
st.pop()
st1.pop()
try:
    print(st1.peek())
except IndexError:
    pass

print(" printing 1st stack", st.items)
print(" printing 2 nd stack", st1.items)
print(" printing 1st stack", st.gitem)
print(" printing 2 nd stack", st1.gitem)
print(" printing using stack", Stack.gitem)
try:
    print(st1.peek())
    print(st.peek())
    
except IndexError:
    print("stack is empty")