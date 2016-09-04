from sets import Set
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tempSet = Set()
    	for i in xrange(len(nums)):
    		if nums[i] in tempSet:
    			tempSet.discard(nums[i])
    		else: 
    			tempSet.add(nums[i])
    	return tempSet.pop()
        