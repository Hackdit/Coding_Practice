class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        for i in citations:
            if i<n:
                n-=1
        return n