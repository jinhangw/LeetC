class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 1):
            return True
        res = 0
        while (res != 1):
            if (res == n):
                return False
            if (res != 0):
                n = res
                res = 0
            while (n / 10 != 0):
                res += (n%10)^2
                n /= 10
            res += (n%10)^2
        return True
