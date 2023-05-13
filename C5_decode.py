from HAMMING_new import Hamming_new
import sys


def c5_decode():
    hm = Hamming_new()
    s = ''
    while True:
        if len(s) != 15:
            e = sys.stdin.read(1)
            if e == '':
                break
            s = s + e
            s = s.strip()
        else:
            d = hm.decode(s.strip())
            sys.stdout.write(d)
            sys.stdout.flush()
            s = ''


c5_decode()
"""
lab2_program_windows_amd64.exe -mode=source -phase=3 | python C5_code.py | lab2_program_windows_amd64.exe -mode=channel -phase=3 | python C5_decode.py | lab2_program_windows_amd64.exe -mode=verify -phase=3
"""
