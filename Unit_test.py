import unittest

from test_01 import fizzbuzz

class fizzBuzzTestCases(unittest.TestCase):
       def setUp(self):
           print('Set Up')
       def tearDown(self):
           print('Tear Down')
      # happy flow
       def testCase01(self):
           testResualt = fizzbuzz(15)

           self.assertEqual(testResualt[2],'Fizz')
       def testCase02(self):
           testResualt = fizzbuzz(15)
           self.assertEqual(testResualt[4], 'Buzz')
       def testCase03(self):
            testResual = fizzbuzz(15)
            self.assertEqual(testResual[14], 'Fizz Buzz')
       # sad flow
       def testCase04(self):
           testResualt = fizzbuzz(15)
           self.assertEqual(testResualt[0],'Fizz')

if __name__ == '__main__':
    unittest.main()