class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def OutputList(self):
        if self.length() == 0:
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
        count = 0
        if self.head == None:
            return count

        tracer = self.head
        count = count + 1
        while(tracer.next != None):
            tracer = tracer.next
            count = count + 1
        return count

    def AddTail(self, value):
        node = ListNode(value)
        if self.head == None:
            self.head = node
            return

        if self.tail == None:
            self.tail = node
            self.head.next = self.tail
            return

        self.tail.next = node
        self.tail = self.tail.next

    def AddHead(self, value):
        node = ListNode(value)
        if self.head == None:
            self.head = node
            return

        if self.tail == None:
            self.tail = self.head
            self.head = node
            self.head.next = self.tail
            return

        node.next = self.head
        self.head = node

    def AddPos(self, pos, value):
        # Adding a node into certain position
        if self.length() == 0:
            if pos == 0:
                self.AddHead(value)
                return
            else:
                return
        if pos > self.length():
            return
        if pos == 0:
            self.AddHead(value)
            return
        if pos == self.length():
            self.AddTail(value)
            return

        node = ListNode(value)
        tracer = self.head
        while(pos > 1):  # Move tracer to next pos - 1 times, so it points toward the node beforce target
            tracer = tracer.next
            pos = pos - 1
        node.next = tracer.next
        tracer.next = node

    def PopTail(self):
        if self.length() == 0:
            return
        # store the value of popped node first, cus we will cut it loose later
        output = self.tail.val
        tracer = self.head
        while(tracer.next != self.tail):
            tracer = tracer.next
        self.tail = tracer
        self.tail.next = None
        return output

    def PopHead(self):
        if self.length() == 0:
            return
        # store the value of popped node first, cus we will cut it loose later
        output = self.head.val
        self.head = self.head.next
        return output

    def RemovePos(self, pos):
        # remove a node in certain position
        if self.length() == 0:
            return
        if pos >= self.length():
            return
        if pos == 0:
            self.PopHead()
            return
        if pos == self.length() - 1:
            self.PopTail()
            return
        tracer = self.head
        while(pos > 1):  # Move tracer to next pos - 1 times, so it points toward the node beforce target
            tracer = tracer.next
            pos = pos - 1
        tracer.next = tracer.next.next
        return

    def clear(self):
        self.head = None
        self.tail = None

    def getPos(self, pos):
        # return value of node in certain position
        if self.length() == 0:
            return
        if pos > self.length() - 1:
            return
        tracer = self.head
        while(pos > 0):
            tracer = tracer.next
            pos = pos - 1
        return tracer.val

    def getHead(self):
        if self.length() == 0:
            return
        return self.head.val

    def getTail(self):
        if self.length() == 0:
            return
        return self.tail.val