"""Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1
        maxnum = 2 ** 31 - 1
        if x < 0:
            sign = -1
            x *= -1
        n = int(str(x)[::-1])
        if n > maxnum:
            return 0

        return sign * n


if __name__ == '__main__':
    print(Solution().reverse(1234567332))