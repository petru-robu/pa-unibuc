class Solution:
    def transpose(self, matrix: list[list[int]]):
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    def rotate(self, matrix: list[list[int]]) -> None:
        self.transpose(matrix)
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        print(matrix)
        
        
        

if __name__ == '__main__':
    ans = Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
    print(ans)