import math
import unittest
from test_common import *
import task2

class TestTask2(unittest.TestCase):
  def test_insert(self):
    x = task2.ListADT(10)
    
    ## This should not fail.
    append(x, [1 for i in range(1000)])
    
    ## If the ListADT has renamed the underlying array, or used some other
    ## representation, we can't realy test whether resizing is handled correctly.
    if not hasattr(x, "the_array"):
      raise AttributeError("could not identify underlying array for the ListADT.")

    y = task2.ListADT(10)

    # If we gave a smaller constant, should have become 40.
    self.assertEqual(len(y.the_array), 40, "Allocated array below threshold.")

    # ... and with rounding
    y = task2.ListADT(44)
    for i in range(45):
      y.insert(i, i)
    self.assertEqual(len(y.the_array), 84, "Incorrect grow.") # math.ceil(44 * 1.9)

    # Check shrinking
    for i in range(25):
      y.delete(len(y)-1)
    self.assertTrue(len(y.the_array) == 42, "Incorrect shrink.")

    # My additional test cases:
    # Check if input size is not greater then or equal to 40
    x = task2.ListADT(25)
    y = task2.ListADT(12)

    self.assertTrue(len(y.the_array) == 40, "Incorrect initial size")
    self.assertTrue(len(x.the_array) == 40, "Incorrect initial size.")

    x = task2.ListADT(50)
    self.assertTrue(len(x.the_array) == 50, "Incorrect initial size")
    # Check growth
    y = task2.ListADT(40)

    for i in range(41):
      y.insert(i, i)
    self.assertEqual(len(y.the_array), 76, "Incorrect grow.") # math.ceil(44 * 1.9)

    for i in range(41,77):
      y.insert(i, i)
    self.assertEqual(len(y.the_array), 145, "Incorrect grow.") # math.ceil(76 * 1.9)

    # Check shrink
    for i in range(10):
      y.delete(len(y)-1)
    self.assertTrue(len(y.the_array) == 145, "Incorrect shrink.")

    y = task2.ListADT(40)

    for i in range(41):
      y.insert(i, i)
    self.assertEqual(len(y.the_array), 76, "Incorrect grow.") # math.ceil(44 * 1.9)

    for i in range(15):
      y.delete(len(y)-1)
    self.assertTrue(len(y.the_array) == 76, "Incorrect shrink.")






if __name__ == '__main__':
  unittest.main()
