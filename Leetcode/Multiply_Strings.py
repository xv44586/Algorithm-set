"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

    tips:
        转化成两两十以内数相乘，同时保持对应的位数（10 **index)
        将结果中同位相加
        转化为str

"""


class Solution(object):
    @staticmethod
    def conv(num1):
        return {index: v for index, v in enumerate(reversed(num1))}

    @staticmethod
    def multi_with_index(item1, item2):
        # item ->(index,v)
        i1, v1 = item1
        i2, v2 = item2

        index = i1 + i2
        v = int(v1) * int(v2)
        a, b = divmod(v, 10)
        if a:
            return (index + 1, a), (index, b)

        return None, (index, b)

    @staticmethod
    def add_with_index(item1, item2):
        i1, v1 = item1
        i2, v2 = item2
        assert i1 == i2, 'diff  index apply add'

        v = v1 + v2
        a, b = divmod(v, 10)
        if a:
            return (i1 + 1, a), (i1, b)
        else:
            return None, (i1, b)

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        from collections import defaultdict
        d1 = self.conv(num1)
        d2 = self.conv(num2)
        values = defaultdict(list)  # values contains {index: values_list}
        # do multiply
        for item1 in tuple(d1.items()):
            for item2 in tuple(d2.items()):
                v1, v2 = self.multi_with_index(item1, item2)
                values[v2[0]].append(v2[1])
                if v1:
                    values[v1[0]].append(v1[1])
        # do add for the same index
        for key in range(len(num1) + len(num2)):
            if values.get(key, False):
                v_list = values[key]
                while len(v_list) > 1:
                    sum1, sum2 = self.add_with_index((key, v_list.pop()), (key, v_list.pop()))
                    values[sum2[0]].append(sum2[1])
                    if sum1:
                        values[sum1[0]].append(sum1[1])

        v_str = [0 for i in range(len(num1) + len(num2) + 1)]
        # combine values
        for index, v in values.items():
            v_str[index] = v[0]
        # remove zero in max indexes
        for num in v_str[::-1]:
            if not num:
                v_str.pop()
                continue
            break
        # value equal 0
        if not v_str:
            return '0'

        return ''.join([str(s) for s in v_str[::-1]])
