class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        n=len(citations)
        count=0
        for i in citations:
            if i<n:
                n-=1
        return n