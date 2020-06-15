import unittest
from Linked_List import ListNode, Linked_List


class LinkedListTest(unittest.TestCase):
    def test_AddTail(self):
        temp = Linked_List()
        for i in range(100):
            temp.AddTail(i)
        result = list(range(100))
        self.assertEqual(temp.OutputList(), result)

    def test_AddHead(self):
        temp = Linked_List()
        for i in range(100):
            temp.AddHead(i)
        result = list(range(100))[::-1]
        self.assertEqual(temp.OutputList(), result)

    def test_AddPos(self):
        temp = Linked_List()
        temp.AddTail(10)
        temp.AddTail(20)
        temp.AddTail(30)
        temp.AddTail(40)
        temp.AddTail(50)
        temp.AddPos(0, 5)  # head
        temp.AddPos(6, 100)  # tail
        temp.AddPos(3, 25)  # middle
        result = [5, 10, 20, 25, 30, 40, 50, 100]
        self.assertEqual(temp.OutputList(), result)
        # --------------------------------------------------
        # Position Out of bound test
        temp.AddPos(10, 200)
        temp.AddPos(15, 250)
        temp.AddPos(20, 300)
        temp.AddPos(25, 350)
        temp.AddPos(30, 400)
        temp.AddPos(35, 450)
        self.assertEqual(temp.OutputList(), result)

    def test_PopTail(self):
        temp = Linked_List()
        for i in range(5):
            temp.AddHead(i)
        PopOutput = []
        for i in range(5):
            PopOutput.append(temp.PopTail())
        result = [0, 1, 2, 3, 4]
        self.assertEqual(PopOutput, result)
        # ----------------------------------------------------
        # Make Sure the list will be empty when all nodes are popped
        self.assertEqual(temp.OutputList(), [])

    def test_PopHead(self):
        temp = Linked_List()
        for i in range(5):
            temp.AddHead(i)
        PopOutput = []
        for i in range(5):
            PopOutput.append(temp.PopHead())
        result = [4, 3, 2, 1, 0]
        self.assertEqual(PopOutput, result)
        # ----------------------------------------------------
        # Make Sure the list will be empty when all nodes are popped
        self.assertEqual(temp.OutputList(), [])

    def test_RemovePos(self):
        temp = Linked_List()

        # All remove head
        for i in range(10):
            temp.AddTail(i)
        for i in range(10):
            temp.RemovePos(0)
        self.assertEqual(temp.OutputList(), [])

        # All remove tail
        for i in range(10):
            temp.AddTail(i)
        for i in list(range(10))[::-1]:
            temp.RemovePos(i)
        self.assertEqual(temp.OutputList(), [])

        # remove empty list
        temp.RemovePos(0)
        self.assertEqual(temp.OutputList(), [])

        # random removal
        for i in range(10):
            temp.AddTail(i)
        temp.RemovePos(3)
        temp.RemovePos(7)
        temp.RemovePos(4)
        result = [0, 1, 2, 4, 6, 7, 9]
        self.assertEqual(temp.OutputList(), result)



if __name__ == "__main__":
    unittest.main()
