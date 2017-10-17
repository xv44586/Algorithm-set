"""
Determine whether an integer is a palindrome. Do this without extra space.


"""


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        if x < 10:
            return True
        x = str(x)
        mid, r = divmod(len(x), 2)
        if x[:mid] == x[mid + r:][::-1]:
            return True
        return False



if __name__ == '__main__':
    print(Solution().isPalindrome(1221))
