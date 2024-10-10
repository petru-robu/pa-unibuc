import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        mx = max(a, b)
        cnt = 0
        for d in range(1, mx+1):
            if a % d==0 and b % d==0:
                cnt+=1
        return cnt
    
if __name__ == "__main__":
    s = Solution()
    print(s.commonFactors(885, 885))