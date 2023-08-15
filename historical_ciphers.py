import random
import secrets
import string
from operator import itemgetter
from utilities import letter_frequencies, average_letter_frequencies


class VigenereCipher:
    """
    Poly-alphabetic shift cipher
    """

    @staticmethod
    def validate_key(key):
        return key.isalpha() and key.isupper()

    @staticmethod
    def generate_key(period):
        return ''.join(secrets.choice(string.ascii_uppercase) for i in range(period))

    def __init__(self, key=generate_key(26)):
        self.key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, k):
        if not self.validate_key(k):
            raise ValueError
        self._key = k

    def encrypt(self, message):
        return ''.join(
            chr(ord('a') + (ord(ch) - ord('a') + ord(self.key[idx % len(self.key)]) - ord('A')) % 26) for idx, ch in
            enumerate(message)).upper()

    def decrypt(self, ciphertext):
        return ''.join(
            chr(ord('A') + (ord(ch) - ord('A') - (ord(self.key[idx % len(self.key)]) - ord('A')) + 26) % 26) for idx, ch
            in enumerate(ciphertext)).lower()


class ShiftCipher(VigenereCipher):
    @staticmethod
    def validate_shift(shift):
        return 0 <= shift < 26

    def __init__(self, shift=0):
        super().__init__(chr(ord('A') + shift))
        self.shift = shift

    @property
    def shift(self):
        return self._shift

    @shift.setter
    def shift(self, s):
        if not self.validate_shift(s):
            raise ValueError
        self._shift = s


class CaesarsCipher(ShiftCipher):
    def __init__(self):
        super().__init__(3)


class MonoAlphabaticSubstituionCipher:
    @staticmethod
    def validate_key(key):
        if len(key) != 26:
            return False

        return string.ascii_uppercase == ''.join(sorted(key))

    @staticmethod
    def generate_key():
        k = list(string.ascii_uppercase)
        random.shuffle(k)
        return ''.join(k)

    def __init__(self, key=generate_key()):
        self.key = key
        # sort key indices, which map to the plaintext alphabetic characters
        self.key_indices = [e[0] for e in sorted(enumerate(self.key), key=itemgetter(1))]

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, k):
        if not self.validate_key(k):
            raise ValueError
        self._key = k

    def encrypt(self, message):
        return ''.join(self.key[ord(ch) - ord('a')] for ch in message)

    def decrypt(self, ciphertext):
        return ''.join(chr(ord('a') + self.key_indices[ord(ch) - ord('A')]) for ch in ciphertext).lower()

    @staticmethod
    def ciphertext_only(ciphertext):
        freqs = letter_frequencies(m)
        print(freqs)
        avg_freqs = average_letter_frequencies()
        print(avg_freqs)
        pairs = zip(freqs.keys(), avg_freqs.keys())
        recovered_key = ''.join(p[0] for p in sorted(pairs, key=itemgetter(1)))
        print(recovered_key)
        return MonoAlphabaticSubstituionCipher(recovered_key).decrypt(ciphertext)


cipher = CaesarsCipher()
c = cipher.encrypt('begin the attack now')
print(c)
m = cipher.decrypt(c)
print(m)

m = 'JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQVFGWJVFPFOLFHGQVWVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX'
print(len(m))
print(MonoAlphabaticSubstituionCipher.ciphertext_only(m))
cipher = MonoAlphabaticSubstituionCipher('HCJKFEYVBNXZPLOMTGWQIASDRU')
print(cipher.decrypt(m))

cipher = MonoAlphabaticSubstituionCipher('XEUADNBKVMROCQFSYHWGLZIJPT')
c = cipher.encrypt('tellhimaboutme')
print(c)
m = cipher.decrypt(c)
print(m)

cipher = VigenereCipher('cafe'.upper())
c = cipher.encrypt('tellhimaboutme')
print(c)
m = cipher.decrypt(c)
print(m)
