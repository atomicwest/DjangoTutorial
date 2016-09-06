import unittest

def adder(a,b):
    return a + b

class TestAdder(unittest.TestCase):
    def test_main(self):
        self.assertEqual(adder(3,4), 7)
        
if __name__ == '__main__':
    unittest.main()
