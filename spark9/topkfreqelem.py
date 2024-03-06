class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res=dict()
        for i in range(len(nums)): #increasing count of each element that exists, add to dict
            if nums[i] in res:
                res[nums[i]]+=1
            else:
                res[nums[i]]=1
        x=list()
        for i in res: # created 2d list from dict
            x.append([i, res[i]])
        x.sort(key=lambda x:x[1], reverse=True)
        y=list()
        for i in range(k): #only taken 1st value i.e. keys of 2d list in new list for printing
            y.append(x[i][0])
        return y