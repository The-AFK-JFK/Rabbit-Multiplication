from rabbits import rabbits,RabbitOutOfRangeError
import unittest
import timeit

class RabbitTests(unittest.TestCase):
    
    def test_zero(self):
        'Should fail with 0'
        self.assertRaises(RabbitOutOfRangeError, rabbits, 0)

    def test_negative(self):
        'Should fail with negative input'
        self.assertRaises(RabbitOutOfRangeError, rabbits, -1) 

    def test_non_integral(self):
        'Should fail with non-integer input'
        self.assertRaises(RabbitOutOfRangeError, rabbits, 'nero') 

    def test_too_large(self):
        'Should fail with large input'
        self.assertRaises(RabbitOutOfRangeError, rabbits, 5000)

if __name__=="__main__":
    unittest.main()
