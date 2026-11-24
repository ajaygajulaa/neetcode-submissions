class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(0, len(nums)):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]]=i
        return False