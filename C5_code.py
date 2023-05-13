from HAMMING_new import Hamming_new
import sys


def c5_code():
    hm = Hamming_new()
    s = ''
    while True:
        if len(s) != 11:
            e = sys.stdin.read(1)
            if e == '':
                break
            if e == '0' or e == '1':
                s = s + e
                s = s.strip()
        else:
            c = hm.code(s.strip())
            sys.stdout.write(c)
            sys.stdout.flush()
            s = ''


c5_code()
# """
# 00111110000
# 00101010000
# 00101010000
# 00000000000
# 11110011110
# 10010010010
# 11110011110
# 00000000000
# 00011110000
# 00010010000
# 00010010000
# """
