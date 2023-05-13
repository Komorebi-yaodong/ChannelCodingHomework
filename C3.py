from HAMMING_new import Hamming_new
from random import randint


def tes1():
    filename = 'hamming_15_11.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        c_list = []
        d_list = []
        while True:
            line = f.readline()
            if line == '':
                break
            line = line.strip().split(',')
            c_list.append(line[0].strip())
            d_list.append(line[1].strip())

    hm = Hamming_new()
    judge = True
    for i in range(len(d_list)):
        if d_list[i] != hm.code(c_list[i]):
            judge = False
            print(c_list[i], 'should be', d_list[i], 'but', hm.code(c_list[i]))
    if judge:
        print('Pass test1 !')
    else:
        print('Wrong in test1 !')


def tes2():
    hm = Hamming_new()
    c = [bin(i)[2:].rjust(11, '0') for i in range(1 << 11)]
    judge = True
    for item in c:
        x = hm.code(item)
        y = hm.decode(x)
        if item != y:
            print(f'Wrong:{item} coded as {x} , decoded as {y} not initial...')
            judge = False
    if judge:
        print('Pass test2 !')
    else:
        print('Wrong in test2 !')


def tes3():
    hm = Hamming_new()
    a = 0
    b = 1 << 11
    judge = True
    for times in range(100):
        i = randint(a, b)
        s = bin(i)[2:].rjust(11, '0')
        s_c = hm.code(s)
        j = randint(0, 14)
        s_l = hm.s2l(s_c)
        s_l[j] = s_l[j] ^ 1
        s_c = hm.l2s(s_l)
        s_d = hm.decode(s_c)
        if s_d != s:
            judge = False
            print(s, 'but', s_d)
    if judge:
        print('Pass test3 !')
    else:
        print('Wrong in test3 !')


if __name__ == "__main__":
    tes1()
    tes2()
    tes3()
