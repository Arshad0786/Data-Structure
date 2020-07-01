import unittest
from Stack import Stack


class StackTest(unittest.TestCase):
    def test_push(self):
        temp = Stack()
        for i in range(100):
            temp.push(i)
        self.assertEqual(temp.outputStack(), list(range(100))[::-1])

    def test_pop(self):
        temp = Stack()
        for i in range(100):
            temp.push(i)
        PopOutput = []
        for i in range(100):
            PopOutput.append(temp.pop())
        self.assertEqual(temp.outputStack(), [])
        self.assertEqual(PopOutput, list(range(100)[::-1]))

    def test_clear(self):
        temp = Stack()
        for i in range(100):
            temp.push(i)
        self.assertEqual(temp.outputStack(), list(range(100))[::-1])
        temp.clear()
        self.assertEqual(temp.outputStack(), [])


if __name__ == "__main__":
    unittest.main()
