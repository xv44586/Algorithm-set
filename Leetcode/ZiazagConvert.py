"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

# split list into new list that in special numbers of members


class Solution(object):
    def split_to_list(self, s, num):
        num = num * 2 - 2
        if not num:
            return [s]
        r = []
        for i in range(0, len(s), num):
            r.append(list(s[i: i + num]))

        return r

    def convert(self, s, num):
        if len(s) < 2 or num <= 1:
            return s
        c = self.split_to_list(s, num)
        result = [[] for i in range(num)]
        for cc in c:
            for i, v in enumerate(cc):
                if i < num:
                    result[i].append(v)
                else:
                    result[2 * num - i - 2].append(v)
        s = ''
        for l in result:
            s += ''.join(l)
        return s


if __name__ == '__main__':
    print(Solution().convert('PAYPALISHIRING', 3))
