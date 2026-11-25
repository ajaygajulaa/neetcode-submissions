class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k =[]
        prod = 1
        for i in nums:
            k.append(prod)
            prod = prod*i
        # print(k)
        pro= 1
        for i in range(len(nums)-1,-1,-1):
            k[i]= k[i]*pro
            pro = pro*nums[i]
        return k