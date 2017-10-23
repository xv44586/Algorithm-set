"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask
yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to
gather all the input requirements up front.

"""


class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        s = s.split()[0]
        if len(s) == 0:
            return 0
        sign = 1
        #         while s[0] in ['-', '+']:
        if s[0] in ['-', '+']:
            sign *= -1 if s[0] == '-' else 1
            s = s[1:]
        if len(s) == 0 or s[0] in ['-', '+']:
            return 0
        # print(s)
        ret, i = 0, 0
        for x in s:
            # print(x)
            if not x.isdigit():
                break

            ret = ret * 10 + ord(x) - ord('0')

        return max(-2 ** 31, min(ret * sign, 2 ** 31 - 1))


if __name__ == '__main__':
    print(Solution().myAtoi('-123'))
