class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.count = 0

    def outputQueue(self):
        a = []
        if self.count == 0:
            return a
        tracer = self.head
        while tracer.next != None:
            a.append(tracer.val)
            tracer = tracer.next
        a.append(tracer.val)
        return a

    def length(self):
        if self.head == None:
            return 0
        count = 0
        tracer = self.head
        while tracer.next != None:
            count = count + 1
            tracer = tracer.next
        count = count + 1
        return count

    def push(self, val):
        node = ListNode(val)
        if self.count == 0:
            self.head = node
            self.count = self.count + 1
            return
        node.next = self.head
        self.head = node
        self.count = self.count + 1
        return

    def pop(self):
        output = None
        if self.count == 0:
            return
        if self.count == 1:
            output = self.head.val
            self.head = None
            self.count = self.count - 1
            return output
        if self.count == 2:
            output = self.head.next.val
            self.head.next = None
            return output
        tracer = self.head
        while tracer.next.next != None:
            tracer = tracer.next
        output = tracer.next.val
        tracer.next = None
        self.count = self.count - 1
        return output

"""
a = Queue()
a.push(10)
a.push(20)
a.push(30)
a.push(40)
a.push(50)
print(a.count)
print(a.outputQueue())
print("---------------------")
print(a.Pop())
print(a.Pop())
print(a.Pop())
print(a.Pop())
print(a.Pop())
print(a.count)
print(a.outputQueue())
"""