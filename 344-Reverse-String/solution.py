class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverseS = ""
        for i in xrange(len(s)):
            reverseS += s[len(s)-1-i]
        return reverseS