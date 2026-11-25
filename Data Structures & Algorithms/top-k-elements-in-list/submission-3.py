class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}
        n = len(nums)
        for i, val in enumerate(nums):
            if val not in dic:
                dic[val]=1
            else:
                dic[val] += 1
        # top_scores = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        # element= list(top_scores.keys())
        # return element[0:k]

        buckt = [ []for _ in range(n+1)]
        for key, val in dic.items():
            buckt[val].append(key)
        result = []
        for i in range(len(buckt)-1,0,-1):
            for num in buckt[i]:
                result.append(num)
                if len(result)== k:
                    return result
            
            
        
        
        