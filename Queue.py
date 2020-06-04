class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def outputQueue(self):
        a = []
        if self.count() == 0:
            return a
        tracer = self.head
        while tracer.next != None:
            a.append(tracer.val)
            tracer = tracer.next
        a.append(tracer.val)
        return a

    def count(self):
        if self.head == None:
            return 0
        count = 0
        tracer = self.head
        while(tracer.next != None):
            count = count + 1
            tracer = tracer.next
        count = count + 1
        return count

    def push(self, val):
        node = ListNode(val)
        if self.count() == 0:
            self.head = node
            self.head.next = self.tail
            return
        if self.count() == 1:
            node.next = self.head
            self.tail = self.head
            self.head = node
            return
        node.next = self.head
        self.head = node
        return


a = Queue()
a.push(10)
print(a.count())
a.push(20)
print(a.count())
a.push(30)
print(a.count())
a.push(40)
print(a.count())
a.push(50)
print(a.count())
print(a.outputQueue())
