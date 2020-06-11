import unittest
from Linked_List import ListNode, Linked_List


class QueueTest(unittest.TestCase):
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
        temp.AddPos(0, 5)
        temp.AddPos(6, 100)
        temp.AddPos(3, 25)
        result = [5, 10, 20, 25, 30, 40, 50, 100]
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


if __name__ == "__main__":
    unittest.main()
