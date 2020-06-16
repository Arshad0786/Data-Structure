class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def OutputList(self):
        """
        return the whole linked list as an array
        """
        if self.count == 0:
            return []
        a = []
        tracer = self.head
        while tracer.next != None:
            a.append(tracer.val)
            tracer = tracer.next
        a.append(tracer.val)
        return a

    def length(self):
        # return the length of the Linked List
        return self.count

    def AddTail(self, value):
        node = ListNode(value)
        if self.head == None:
            self.head = node
            self.count = self.count + 1
            return

        if self.tail == None:
            self.tail = node
            self.head.next = self.tail
            self.count = self.count + 1
            return

        self.tail.next = node
        self.tail = self.tail.next
        self.count = self.count + 1

    def AddHead(self, value):
        node = ListNode(value)
        if self.head == None:
            self.head = node
            self.count = self.count + 1
            return

        if self.tail == None:
            self.tail = self.head
            self.head = node
            self.head.next = self.tail
            self.count = self.count + 1
            return

        node.next = self.head
        self.head = node
        self.count = self.count + 1



    def AddPos(self, pos, value):
        # Adding a node into certain position
        if self.count == 0:
            if pos == 0:
                self.AddHead(value)
                return
            else:
                return
        if pos > self.count:
            return
        if pos == 0:
            self.AddHead(value)
            return
        if pos == self.count:
            self.AddTail(value)
            return

        node = ListNode(value)
        tracer = self.head
        while(pos > 1):  # Move tracer to next pos - 1 times, so it points toward the node beforce target
            tracer = tracer.next
            pos = pos - 1
        node.next = tracer.next
        tracer.next = node
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
        # store the value of popped node first, cus we will cut it loose later
        output = self.tail.val
        tracer = self.head
        while(tracer.next != self.tail):
            tracer = tracer.next
        self.tail = tracer
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
        # store the value of popped node first, cus we will cut it loose later
        output = self.head.val
        self.head = self.head.next
        self.count = self.count - 1
        return output

    def RemovePos(self, pos):
        # remove a node in certain position
        if self.count == 0:
            return
        if pos >= self.count:
            return
        if pos == 0:
            self.PopHead()
            return
        if pos == self.count - 1:
            self.PopTail()
            return
        tracer = self.head
        while(pos > 1):  # Move tracer to next pos - 1 times, so it points toward the node beforce target
            tracer = tracer.next
            pos = pos - 1
        tracer.next = tracer.next.next
        self.count = self.count - 1
        return

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0

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

    def getHead(self):
        if self.count == 0:
            return
        return self.head.val

    def getTail(self):
        if self.count == 0:
            return
        return self.tail.val
