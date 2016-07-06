class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        while (num / 10 != 0):
            res += num % 10
            num /= 10
        res += num
        if (res / 10 != 0):
            return self.addDigits(res)
        else:
            return res
            