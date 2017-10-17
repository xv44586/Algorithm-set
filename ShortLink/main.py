"""
url -> int -> mod -> 62 ** 4 or 5 -> char list
0-9,a-z,A-Z  ->62
"""


class Convert(object):
    SCALE = 62

    def __init__(self, url):
        self.url = url

    def convert_url_to_num(self):
        num = 0
        for index, c in enumerate(
                reversed(self.url)):  # almost every url start with http:// or https,revere it to reduce confilict possibility
            num += 3 ** index * ord(c)  # ord('0') = 48 ord('z') = 122 use 3 to avoid different url trans to same num

        return num

    # calculate remainder of num and 62 * length to convert num to length of char list
    @classmethod
    def cal_remainder(cls, num, length=4):
        _, r = divmod(num, cls.SCALE ** length)
        while not cls.check_complict(r):
            length += 1
            _, r = divmod(num, cls.SCALE ** length)

        return r

    @classmethod
    def trans_num_from_10_to_62(cls, num):
        n = []
        while num >= cls.SCALE:
            num, r = divmod(num, cls.SCALE)
            n.append(r)

        n.append(num)

        return ''.join([cls.char(i) for i in reversed(n)])

    @staticmethod
    def check_complict(remainder):
        return True

    def __call__(self, *args, **kwargs):
        num = self.convert_url_to_num()
        remainder = self.cal_remainder(num)
        char_list = self.trans_num_from_10_to_62(remainder)
        print(char_list)

    @staticmethod
    def char(num):
        num_0 = num + ord('0')
        if num_0 <= ord('9'):
            return chr(num_0)
        else:
            num_a = num + ord('a') - 10
            if num_a <= ord('z'):
                return chr(num_a)
            else:
                num_A = num + ord('A') - 10 - 26
                if num_A <= ord('Z'):
                    return chr(num_A)
                else:
                    print('not in the a-z 0-9 A-Z')

if __name__ == '__main__':
    Convert('http://localhost:888/notebooks/Untitled54.ipynb?kernel_name=python3')()