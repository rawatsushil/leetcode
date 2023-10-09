# https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/


class RabinKarp:
    def __init__(self):
        self.pattern_hash = 0
        self.text_hash = 0
        self.chars = 256
        self.q = 101

    def calculate_hash(self, txt):
        _hash = 0
        for i in range(len(txt)):
            _hash = (_hash*self.chars + ord(txt[i])) % self.q
        return _hash

    @staticmethod
    def is_substring_equal(str1, str2):
        for i in range(len(str1)):
            if not (str1[i] == str2[i]):
                return False
        return True

    def is_pattern_found(self, pat, txt):
        M = len(pat)
        N = len(txt)
        h = self.chars**(len(pat)-1)

        self.pattern_hash = self.calculate_hash(pat)
        self.text_hash = self.calculate_hash(txt[:len(pat)])

        for i in range(N-M+1):
            if self.text_hash == self.pattern_hash:
                if self.is_substring_equal(pat, txt[i:i+M]):
                    return True
            if i < N-M:
                self.text_hash = (self.chars*(self.text_hash - h*ord(txt[i])) + ord(txt[i+M]))%self.q
        return False


pattern = "abcd"
text = "eftgtgrfraaabcd"
print(RabinKarp().is_pattern_found(pattern, text))
