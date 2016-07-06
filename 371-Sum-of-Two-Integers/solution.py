class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if (b>0):
            while (b > 0):
                a++
                b--
        else:
            while (b < 0):
                a--
                b++
        return a
        