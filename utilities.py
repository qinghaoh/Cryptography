# a-z
import string
from collections import Counter
from operator import itemgetter

LETTER_FREQUENCIES = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4, 6.7, 7.5, 1.9, 0.1, 6.0,
                      6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]


def letter_counts(ciphertext):
    return Counter(list(ciphertext))


def letter_frequencies(ciphertext):
    counter = letter_counts(ciphertext)
    total = counter.total()
    d = dict(zip(string.ascii_uppercase, [0] * 26)) | {k: v / total * 100 for k, v in counter.items()}
    return dict(sorted(d.items(), key=itemgetter(1), reverse=True))


def average_letter_frequencies():
    return dict(sorted(zip(string.ascii_lowercase, LETTER_FREQUENCIES), key=itemgetter(1), reverse=True))
