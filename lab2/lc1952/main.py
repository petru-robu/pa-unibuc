import math

class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def isThree(self, n: int) -> bool:
        r = int(math.sqrt(n))

        if r * r == n and self.isPrime(r):
            return True
        else:
            return False
        
    
if __name__ == "__main__":
    n = 14
    s = Solution()
    print(s.isThree(n))