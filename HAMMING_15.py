class Hamming_15:
    def __init__(self):

        self.H = [
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.G = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        ]
        self.C_list = []
        self.C_dir = {}
        self.D_dir = {}
        self.C_total_list = []
        self.C_total_dir = {}
        self.D_total_dir = {}

    def matix_mul(self, A, B):
        """
        矩阵乘法
        :param A:
        :param B:
        :return:
        """
        res = []
        r_num = len(A)
        times = len(A[0])
        c_num = len(B[0])
        for i in range(r_num):
            line = []
            for j in range(c_num):
                item = 0
                for t in range(times):
                    item = item ^ (A[i][t] & B[t][j])
                line.append(item)
            res.append(line[:])
        return res

    def matix_T(self, A):
        """
        矩阵转置
        :param A:
        :return:
        """
        r_num = len(A)
        c_num = len(A[0])
        res = []
        for i in range(c_num):
            line = []
            for j in range(r_num):
                line.append(A[j][i])
            res.append(line[:])
        return res

    def matix_show(self, A):
        """
        矩阵展示
        :param A:
        :return:
        """
        print('show_matix:')
        for line in A:
            for e in line:
                print(e, end=' ')
            print()
        print()
        return

    def s2l(self, c: str):
        """
        字符串转一维列表
        :param c:
        :return:
        """
        res = []
        for i in c:
            res.append(int(i))
        return res

    def l2s(self, l: list):
        """
        一维列表转字符串
        :param l:
        :return:
        """
        res = ''
        for i in l:
            res = res + str(i)
        return res

    def get_code(self, c: list):
        """
        :param c: 信号源码列表，c内元素为字符串
        :return: hamming编码列表
        """

        for e in c:
            num = int(e, 2)
            e_list = [0] * 15
            count = 0
            while num > 0:
                flag = num & 1
                if flag == 1:
                    for i in range(15):
                        e_list[i] = e_list[i] ^ self.G[10 - count][i]
                count += 1
                num = num >> 1
            e_new = self.l2s(e_list)
            self.C_list.append(e_new)

        for i in range(len(c)):
            self.C_dir[c[i]] = self.C_list[i]
            self.D_dir[self.C_list[i]] = c[i]

        return self.C_list

    def get_total_code(self):
        C = [bin(i)[2:].rjust(11, '0') for i in range(1 << 11)]

        for e in C:
            num = int(e, 2)
            e_list = [0] * 15
            count = 0
            while num > 0:
                flag = num & 1
                if flag == 1:
                    for i in range(15):
                        e_list[i] = e_list[i] ^ self.G[10 - count][i]
                count += 1
                num = num >> 1
            e_new = self.l2s(e_list)
            self.C_total_list.append(e_new)

        for i in range(len(C)):
            self.C_total_dir[C[i]] = self.C_total_list[i]
            self.D_total_dir[self.C_total_list[i]] = C[i]

        return self.C_total_list

    def check(self, c: str):
        c_l = [self.s2l(c)]
        r_l = self.matix_mul(c_l, self.matix_T(self.H))[0]
        r_l.reverse()
        r = int(self.l2s(r_l), 2)
        print(r)
        if r == 0:
            return True, c
        elif 1 <= r <= 15:
            c_l[0][r - 1] = c_l[0][r - 1] ^ 1
            res = self.l2s(c_l[0])
            return False, res
        else:
            return False, None

    def correct(self, c: str):
        c_l = [self.s2l(c)]
        r_l = self.matix_mul(c_l, self.matix_T(self.H))[0]
        r_l.reverse()
        r = int(self.l2s(r_l), 2)
        if r == 0:
            return c
        elif 1 <= r <= 15:
            c_l[0][r - 1] = c_l[0][r - 1] ^ 1
            res = self.l2s(c_l[0])
            return res
        else:
            return None

    def decode(self, c: str):
        if self.D_dir == {}:
            print('get_code first please...')
        else:
            return self.D_dir[c]

    def code(self, c: str):
        if self.C_dir == {}:
            print('get_code first please...')
        else:
            return self.C_dir[c]


if __name__ == "__main__":
    s = ['0', '1']
    hm = Hamming_15()
    s_l = hm.get_code(s)
    print(s_l)
    print(hm.C_dir)
