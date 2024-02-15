import unittest
from stack import MyStack

class TestMyStack(unittest.TestCase):
    def test_init(self):
        temp = MyStack()
        self.assertEqual(len(temp._array), 2)
        self.assertIsNone(temp._array[0])
        self.assertIsNone(temp._array[1])
        self.assertEqual(temp._size, 0)

    def test_is_empty(self):
        stack = MyStack()
        self.assertTrue(stack.is_empty())
        stack.push('test')
        self.assertFalse(stack.is_empty())

    def test_expand(self):
        stack = MyStack()
        stack.push('test1')
        stack.push('test2')
        # Trigger expand by adding more items than initial capacity
        stack.push('test3')
        self.assertEqual(len(stack._array), 4)  # Check if capacity doubled
        # Verify that items are intact after expansion
        self.assertEqual(stack.pop(), 'test3')
        self.assertEqual(stack.pop(), 'test2')
        self.assertEqual(stack.pop(), 'test1')

    def test_push(self):
        stack = MyStack()
        stack.push('test')
        self.assertEqual(stack._size, 1)
        self.assertEqual(stack.top(), 'test')

    def test_pop(self):
        stack = MyStack()
        stack.push('test1')
        stack.push('test2')
        self.assertEqual(stack.pop(), 'test2')
        self.assertEqual(stack.pop(), 'test1')
        self.assertIsNone(stack.pop())  # Test popping from an empty stack

    def test_top(self):
        stack = MyStack()
        self.assertIsNone(stack.top())  # Test top on an empty stack
        stack.push('test')
        self.assertEqual(stack.top(), 'test')
        stack.push('another test')
        self.assertEqual(stack.top(), 'another test')
        stack.pop()
        self.assertEqual(stack.top(), 'test')

if __name__ == '__main__':
    unittest.main()

    