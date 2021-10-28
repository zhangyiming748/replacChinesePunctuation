# python中输入字符串,统计字符串中大小写英文字母各有多少个？
class countNum(object):
    def __init__(self):
        s = input("input a string")
        self.s = s

    def judge(self):
        bigger = 0
        smaller = 0
        for i in self.s:
            if i < 'A' or i > 'z':
                continue
            elif 'A' < i < 'Z':
                bigger += 1
            elif 'a' < i < 'z':
                smaller += 1
        return bigger, smaller


if __name__ == '__main__':
    p = countNum()
    big, small = p.judge()
    print("大写字母%d个" % big)
    print("小写字母%d个" % small)
