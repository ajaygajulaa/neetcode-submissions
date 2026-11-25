class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}
        n = len(nums)
        for i, val in enumerate(nums):
            if val not in dic:
                dic[val]=1
            else:
                dic[val] += 1

        buckt = [ []for _ in range(n+1)]
        for key, val in dic.items():
            buckt[val].append(key)
        # print(buckt)
        result = []
        for i in range(len(buckt)-1,0,-1):
            for num in buckt[i]:
                result.append(num)
                if len(result)== k:
                    # print(result)
                    return result
            
            
        
        
        