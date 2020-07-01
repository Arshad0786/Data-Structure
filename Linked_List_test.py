import unittest
from Linked_List import Linked_List


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
        temp.clear()
        # --------------------------------------------------
        # Pos is head test
        result = []
        for i in range(10):
            temp.AddPos(0, i*10)
            result.append(i*10)
        self.assertEqual(temp.OutputList(), result[::-1])
        temp.clear()
        # --------------------------------------------------
        # Pos is tail test
        result = []
        for i in range(5):
            temp.AddPos(i, i*10)
            result.append(i*10)
        self.assertEqual(temp.OutputList(), result)
        temp.clear()
    
    def test_PopTail(self):
        temp = Linked_List()
        for i in range(10):
            temp.AddHead(i)
        PopOutput = []
        for i in range(10):
            PopOutput.append(temp.PopTail())
        result = list(range(10))
        self.assertEqual(PopOutput, result)
        # ----------------------------------------------------
        # Make Sure the list will be empty when all nodes are popped
        self.assertEqual(temp.OutputList(), [])
    

    def test_PopHead(self):
        temp = Linked_List()
        for i in range(10):
            temp.AddTail(i)
        PopOutput = []
        for i in range(10):
            PopOutput.append(temp.PopHead())
        result = list(range(10))
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
        # --------------------------------------------------
        # Position Out of bound test
        temp.RemovePos(20)
        temp.RemovePos(30)
        temp.RemovePos(40)
        temp.RemovePos(50)
        temp.RemovePos(100)
        self.assertEqual(temp.OutputList(), result)

    def test_clear(self):
        temp = Linked_List()
        for i in range(100):
            temp.AddTail(i)
        self.assertEqual(temp.OutputList(), list(range(100)))
        temp.clear()
        self.assertEqual(temp.OutputList(), [])
        # -----------------------------------------------
        # clear empty list test
        temp.clear()
        self.assertEqual(temp.OutputList(), [])
        # -----------------------------------------------
        # Make sure clear() properly reset the list
        temp.AddHead(10)
        temp.AddHead(20)
        temp.AddHead(30)
        self.assertEqual(temp.OutputList(), [30, 20, 10])

    def test_getHead(self):
        temp = Linked_List()
        for i in range(100):
            temp.AddHead(i)
        self.assertEqual(temp.getHead(), 99)
        # -----------------------------------------------
        # Get head of empty list
        temp.clear()
        self.assertEqual(temp.OutputList(), [])
        self.assertEqual(temp.getHead(), None)
        # -----------------------------------------------
        # Get head of one node list
        temp.clear()
        temp.AddTail(10)
        self.assertEqual(temp.OutputList(), [10])
        self.assertEqual(temp.getHead(), 10)
        # -----------------------------------------------
        # Get head of two nodes list
        temp.clear()
        temp.AddTail(10)
        temp.AddTail(20)
        self.assertEqual(temp.OutputList(), [10, 20])
        self.assertEqual(temp.getHead(), 10)

    def test_getTail(self):
        temp = Linked_List()
        for i in range(100):
            temp.AddHead(i)
        self.assertEqual(temp.getTail(), 0)
        # -----------------------------------------------
        # Get tail of empty list
        temp.clear()
        self.assertEqual(temp.OutputList(), [])
        self.assertEqual(temp.getTail(), None)
        # -----------------------------------------------
        # Get tail of one node list
        temp.clear()
        temp.AddTail(10)
        self.assertEqual(temp.OutputList(), [10])
        self.assertEqual(temp.getTail(), 10)
        # -----------------------------------------------
        # Get tail of two nodes list
        temp.clear()
        temp.AddTail(10)
        temp.AddTail(20)
        self.assertEqual(temp.OutputList(), [10, 20])
        self.assertEqual(temp.getTail(), 20)

    def test_getPos(self):
        temp = Linked_List()
        for i in range(100):
            temp.AddPos(i, i)
        self.assertEqual(temp.OutputList(), list(range(100)))
        for i in range(100):
            self.assertEqual(temp.getPos(i), i)
        # ---------------------------------
        # get Pos from one node list
        temp.clear()
        temp.AddPos(0, 10)
        self.assertEqual(temp.OutputList(), [10])
        self.assertEqual(temp.getPos(0), 10)
        # ---------------------------------
        # get Pos from two nods list
        temp.clear()
        temp.AddPos(0, 10)
        temp.AddPos(1, 20)
        self.assertEqual(temp.OutputList(), [10, 20])
        self.assertEqual(temp.getPos(0), 10)
        self.assertEqual(temp.getPos(1), 20)
        # ---------------------------------
        # get Pos from empty list
        temp.clear()
        self.assertEqual(temp.getPos(0), None)
        # ---------------------------------
        # Position Out of bound test
        temp.clear()
        for i in range(10):
            temp.AddHead(i)
        for i in range(10, 100):
            self.assertEqual(temp.getPos(i), None)


if __name__ == "__main__":
    unittest.main()
