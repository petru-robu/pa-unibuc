class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cnt = 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if grid[i][j] >= 0:
                    break
                else:
                    cnt += 1
        return cnt

if __name__ == '__main__':
    ans = Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    print(ans)