class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
           return 1
        total = 10
        curr = 9

        for i in range(2, n+1):
            total += curr * (11-i)
            curr *= (11-i)

        return total




if __name__ == "__main__":
    n = 3
    sol = Solution()
    print(sol.countNumbersWithUniqueDigits(3))