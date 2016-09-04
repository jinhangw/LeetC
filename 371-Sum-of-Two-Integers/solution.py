class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return int(math.log(math.pow(1.1, a) * math.pow(1.1, b), 1.1))


        