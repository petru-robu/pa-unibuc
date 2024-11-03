class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt, p = 0, 5
        while p <= n:
            cnt += n // p
            p *= 5
        return cnt



if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(30))