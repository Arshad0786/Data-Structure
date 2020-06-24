class StackNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack():
    def __init__(self):
        self.head = None
        self.count = 0

    def outputStack(self):
        if self.count == 0:
            return []
        tracer = self.head
        output = []
        while tracer.next != None :
            output.append(tracer.val)
            tracer = tracer.next
        output.append(tracer.val)
        return output
        
    
    def push(self, val):
        node = StackNode(val)
        if self.count == 0:
            self.head = node
            self.count = self.count + 1
            return
        node.next = self.head
        self.head = node
        self.count = self.count + 1
        return
    
    def pop(self):
        if self.count == 0:
            return
        if self.count == 1:
            output = self.head.val
            self.head = None
            self.count = self.count - 1
            return output
        output = self.head.val
        self.head = self.head.next
        self.count = self.count - 1
        return output
        
    
temp = Stack()
temp.push(10)
temp.push(20)
temp.push(30)
temp.push(40)
temp.push(50)
for i in range(5):
    print("Pop:", temp.pop())
print("----------------")
print(temp.outputStack())