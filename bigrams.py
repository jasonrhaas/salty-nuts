#!/usr/bin/env python

import re
import sys
import logging
from collections import Counter

logging.basicConfig(level=logging.CRITICAL)


def parser(rawstring):
    """Takes a string as input and returns the frequency (>1 or more) of
        bigrams separated by a whitespace.

    :param rawstring: Input string for the function.
    :type rawstring: str

    :returns: Iterable of nicely formatted strings like
              `<word1> <word2> : <count>`
    """
    # lowercase the string
    l_string = rawstring.lower()
    logging.debug(l_string)
    # find pairs of words separated by a whitespace
    r_tups = re.findall(r"([a-zA-Z0-9_']+)\s(?=([a-zA-Z0-9_']+))", l_string)
    logging.debug(r_tups)
    # sort the tuples so they can be grouped
    s_tups = [tuple(sorted(x)) for x in r_tups]
    logging.debug(s_tups)
    # find tuple frequencies
    freq_tups = Counter(s_tups)
    logging.debug(freq_tups)
    # create generator of formatted strings
    for w in freq_tups.most_common():
        if w[1] > 1:
            yield '{0} {1} : {2}'.format(w[0][0], w[0][1], w[1])

if __name__ == '__main__':
    """Takes string input from oneo r more text files.  Pretty prints output from
        the `regparse` function.
    """

    for idx, filename in enumerate(sys.argv[1:]):
        with open(filename) as f:
            logging.info('Filename: {0}'.format(filename))
            stringlist = parser(f.read())
            for s in stringlist:
                print s
