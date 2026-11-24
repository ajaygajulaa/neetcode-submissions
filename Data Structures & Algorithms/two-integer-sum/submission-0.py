class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0, len(nums)):
            s = target - nums[i]
            if s in dic:
                return [dic[s],i] 
            else:
                dic[nums[i]]=i
        
        