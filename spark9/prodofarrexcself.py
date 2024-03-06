class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product=1
        flag=0
        for i in range(len(nums)):
            if nums[i]==0:
                flag+=1
                continue
            else:
                product*=nums[i]
        res=list()
        for i in range(len(nums)):
            if nums[i]==0:
                if flag>1:
                    res.append(0)
                else:
                    res.append(int(product))
            elif flag==0:
                res.append(int(product//nums[i]))
            elif flag>0:
                res.append(0)
        return res