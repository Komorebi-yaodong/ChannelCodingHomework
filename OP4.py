class Hamming_op4:
    def __init__(self):
        pass

    def bit_number(self, s: str):  # 计算现需要多少个校验位
        length = len(s)
        i = 1
        while i + length > (1 << i):
            i += 1
        return i

    def s2l(self, s: str):
        res = []
        for i in s:
            res.append(int(i))
        return res

    def l2s(self, l: list):
        res = ''
        for i in l:
            res = res + str(i)
        return res

    def code(self, s: str):
        count = self.bit_number(s)
        length = len(s) + count
        l = self.s2l(s)
        for i in range(count):
            l.insert((1 << i) - 1, 0)
        for i in range(count):
            # 每个校验位更改
            tmp = 0
            for j in range((1 << i) + 1, length + 1):
                if (j >> i) & 1 == 1:
                    tmp = tmp ^ l[j - 1]
            l[(1 << i) - 1] = tmp
        total = 0
        for i in l:
            total = total ^ i
        l.append(total)
        res = self.l2s(l)
        return res

    def decode(self, s: str):
        length = len(s) - 1
        l = self.s2l(s)
        count = 1
        while length > (1 << count):
            count += 1
        # 校验部分
        correct = ''
        for i in range(count):
            tmp = 0
            for j in range((1 << i), length + 1):
                if (j >> i) & 1 == 1:
                    tmp = tmp ^ l[j - 1]
            correct = str(tmp) + correct
        correct = int(correct, 2)
        total = l[-1]

        if total == 0 and correct != 0:
            print('出现两位错误，无法纠错')
            return None
        if total == 1 and correct != 0:
            print('出现一位错误')
            l[correct - 1] = 1 ^ l[correct - 1]
        for i in range(count):
            l.pop((1 << (count - i - 1)) - 1)
        l.pop(-1)
        res = self.l2s(l)
        return res
