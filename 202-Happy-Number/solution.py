class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 1):
            return True
        res = 0
        copyN = n
        while (n / 10 != 0):
            res += (n%10)^2
            n /= 10
        res += (n%10)^2
        if (res == copyN):
            return False
        else:
            return self.isHappy(res)