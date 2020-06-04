import unittest
from Queue import ListNode, Queue


class QueueTest(unittest.TestCase):
    def test_count_0(self):
        temp = Queue()
        self.assertEqual(temp.count, 0)

    def test_count_1(self):
        temp = Queue()
        temp.push(10)
        self.assertEqual(temp.count, 1)

    def test_count_100(self):
        temp = Queue()
        i = 0
        while(i<100):
            temp.push(i)
            i = i + 1
        self.assertEqual(temp.count, 100)
    
    def test_push_count_0(self):
        temp = Queue()
        temp.push(10)
        self.assertEqual(temp.outputQueue(),[10])
    
    def test_push_count_1(self):
        temp = Queue()
        temp.push(10)
        temp.push(20)
        self.assertEqual(temp.outputQueue(),[20,10])
    
    def test_push_count_100(self):
        temp = Queue()
        for i in range(100):
            temp.push(i)
        self.assertEqual(temp.outputQueue(),list(range(100))[::-1])
    
    def test_pop_count_0(self):
        temp = Queue()
        temp.pop()
        self.assertEqual(temp.outputQueue(),[])
    
    def test_pop_count_1(self):
        temp = Queue()
        temp.push(10)
        self.assertEqual(temp.outputQueue(),[10])
        temp.pop()
        self.assertEqual(temp.outputQueue(),[])
    
    def test_pop_count_100(self):
        temp = Queue()
        for i in range(100):
            temp.push(i)
        self.assertEqual(temp.outputQueue(),list(range(100))[::-1])
        for i in range(100):
            temp.pop()
        self.assertEqual(temp.outputQueue(),[])
        
        


if __name__ == "__main__":
    unittest.main()
