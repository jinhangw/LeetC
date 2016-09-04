from sets import Set
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
    	for i in xrange(len(nums)):
    	    ans ^= nums[i]
    	return ans
        