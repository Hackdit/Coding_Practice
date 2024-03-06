class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        n=len(s)-1
        if n==0:
            return n+1
        while i<n and s[i]==s[n]:
            c=s[i]
            while i<=n and s[i]==c:
                i+=1
            while n>i and s[n]==c:
                n-=1
        return n-i+1