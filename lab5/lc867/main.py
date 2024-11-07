class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])

        ans = []
        for i in range(n):
            ans.append([0]*m)

        for i in range(n):
            for j in range(m):
                ans[i][j] = matrix[j][i]

        return ans             

if __name__ == '__main__':
    s = Solution()
    ans = s.transpose([[1,2,3],[4,5,6]])

    print(ans)