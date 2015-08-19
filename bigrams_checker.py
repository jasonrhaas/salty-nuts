#!/usr/bin/env python

import unittest
import bigrams


class BigramsChecker(unittest.TestCase):
    def test(self):
        answer = "like nuts : 3\nlike you : 3\nare you : 2\ni like : 2"
        with open('nuts.txt') as f:
            self.assertEqual(bigrams.parser(f.read()), answer)

if __name__ == '__main__':
    unittest.main()
