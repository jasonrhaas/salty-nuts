#!/usr/bin/env python

import unittest
import bigrams


class BigramsChecker(unittest.TestCase):
    def test(self):
        answer = [
                    "like nuts : 3",
                    "like you : 3",
                    "are you : 2",
                    "i like : 2"
                    ]
        with open('nuts.txt') as f:
            self.assertEqual(bigrams.parser(f.read()), answer)

if __name__ == '__main__':
    unittest.main()
