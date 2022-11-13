import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task6

class TestTask6(TestCase):
  def test_addfile(self):
    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_simple.txt')
      for word in ['this', 'dictionary', 'words']:
        for i in range(0,len(freq.words)):
          if freq.words[i] == word:
            self.assertEqual(freq.count[i], 1,
          "Incorrect frequency.")

    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_dup.txt')
      for (word, count) in [('words', 3), ('and', 2)]:
        for i in range(0,len(freq.words)):
          if freq.words[i] == word:
            self.assertEqual(freq.count[i], count,
          "Incorrect frequency.")
     
    self.assertTrue(self.check_okay("addfile"))

  def test_rarity(self):
    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_freq.txt')
    
      self.assertEqual(freq.rarity('a'), 0,
        "Incorrect rarity.")

    with self.vis():
      self.assertEqual(freq.rarity('fish'), 2,
        "Incorrect rarity.")
    
    self.assertTrue(self.check_okay("rarity"))

if __name__ == '__main__':
  unittest.main()
