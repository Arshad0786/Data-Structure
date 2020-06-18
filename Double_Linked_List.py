class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Double_Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def OutputList(self):
        if self.count == 0:
            return []
        output = []
        tracer = self.head
        while(tracer.next != None):
            output.append(tracer.val)
            tracer = tracer.next
        output.append(tracer.val)
        return output

    def reverseOutputList(self):
        if self.count == 0:
            return []
        output = []
        tracer = self.tail
        while(tracer.prev != None):
            output.append(tracer.val)
            tracer = tracer.prev
        output.append(tracer.val)
        return output

    def AddTail(self, val):
        node = ListNode(val)
        if self.count == 0:
            self.head = node
            self.tail = node
            self.count = self.count + 1
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.count = self.count + 1

    def AddHead(self, val):
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

    def AddPos(self, pos, val):
        node = ListNode(val)
        if pos > self.count:
            return
        if pos == self.count:
            self.AddTail(val)
            return
        if pos == 0:
            self.AddHead(val)
            return
        tracer = self.head
        while(pos > 1):  # move tracer pos - 1 times
            tracer = tracer.next
            pos = pos - 1
        before = tracer
        after = tracer.next
        before.next = node #link between inserted node and previous node
        node.prev = before
        node.next = after #link between inserted node and next node
        after.prev = node
        self.count = self.count + 1

    def PopTail(self):
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

    def PopHead(self):
        if self.count == 0:
            return
        if self.count == 1:
            output = self.head.val
            self.head = None
            self.tail = None
            self.count = self.count - 1
            return output
        output = self.head.val
        self.head = self.head.next
        self.head.prev = None
        self.count = self.count - 1
        return output

    def RemovePos(self, pos):
        if pos > self.count:
            return
        if pos == self.count -1 :
            self.PopTail()
            return
        if pos == 0:
            self.PopHead()
            return
        tracer = self.head
        while(pos > 1): # move tracer pos - 1 times
            tracer = tracer.next
            pos = pos - 1 
        before = tracer
        after = tracer.next.next
        before.next = after
        after.prev = before
        self.count = self.count - 1

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0

    def getHead(self):
        if self.count == 0:
            return
        return self.head.val
    
    def getTail(self):
        if self.count == 0:
            return
        return self.tail.val
    
    def getPos(self, pos):
        # return value of node in certain position
        if self.count == 0:
            return
        if pos > self.count - 1:
            return
        tracer = self.head
        while(pos > 0):
            tracer = tracer.next
            pos = pos - 1
        return tracer.val

