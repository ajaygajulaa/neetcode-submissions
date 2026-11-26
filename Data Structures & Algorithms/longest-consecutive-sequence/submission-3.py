class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seta = set(nums)
        # if len(nums)==0:
        #     return 0
        maxval = 0
        for i in seta:
            tempval = 1
            if  i - 1 in seta:
                continue
            while ( i + tempval) in seta:
                tempval = tempval+1
            maxval = max(maxval, tempval)
        return maxval
        
        