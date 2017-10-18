"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        for s in strs[0]:
            flag = False

            for st in strs:
                if not st.startswith(res + s):
                    flag = True
                    break
            if flag:
                break
            res += s
        return res
