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
            
            while (n / 10 != 0):
                res += (n%10)^2
                n /= 10
            res += (n%10)^2
            if (res != 0 and res != 1):
                n = res
                res = 0
        return True
