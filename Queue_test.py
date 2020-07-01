import unittest
from Queue import Queue


class QueueTest(unittest.TestCase):
    def test_push(self):
        temp = Queue()
        for i in range(100):
            temp.push(i)
        self.assertEqual(temp.outputQueue(),list(range(100))[::-1])

    def test_pop(self):
        temp = Queue()
        for i in range(100):
            temp.push(i)
        PopOutput = []
        for i in range(100):
            PopOutput.append(temp.pop())
        self.assertEqual(temp.outputQueue(),[])
        self.assertEqual(PopOutput,list(range(100)))
    
    def test_clear(self):
        temp = Queue()
        for i in range(100):
            temp.push(i)
        self.assertEqual(temp.outputQueue(),list(range(100))[::-1])
        temp.clear()
        self.assertEqual(temp.outputQueue(),[])
        for i in range(100):
            temp.push(i)
        self.assertEqual(temp.outputQueue(),list(range(100))[::-1])
              


if __name__ == "__main__":
    unittest.main()
