class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def outputQueue(self):
        output = []
        if self.count == 0:
            return output
        tracer = self.head
        while tracer.next != None:
            output.append(tracer.val)
            tracer = tracer.next
        output.append(tracer.val)
        return output

    def push(self, val):
        node = ListNode(val)
        if self.count == 0:
            self.head = node
            self.tail = node
            self.count = self.count + 1
            return
        node.next = self.head
        self.head.prev = node
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
            self.tail = None
            self.count = self.count - 1
            return output
        output = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.count = self.count - 1
        return output

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
