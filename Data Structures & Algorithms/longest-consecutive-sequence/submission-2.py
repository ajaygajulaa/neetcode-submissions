class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(nums)
        # print(sort)
        if len(nums)==0:
            return 0
        current = sort[0]
        maxval = 1
        tempval = 1
        for i in range(1, len(nums)):
            if sort[i] == current:
                # print("conti")
                continue
            if sort[i] == current+1:
                tempval = tempval+1
                maxval = max(tempval, maxval)
                current = sort[i]
                # print(tempval)
            else:
                current = sort[i]
                # maxval = max(tempval, maxval)
                tempval = 1
                # print("else condi")
        return maxval
        
        