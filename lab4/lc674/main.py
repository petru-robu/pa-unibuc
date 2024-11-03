class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        i = 0
        l = 0
        maxim = -1
        for i in range(len(nums)-1):
            l += 1
            if nums[i] > nums[i+1]:
                maxim =  max(maxim, l)
                l = 0

        maxim =  max(maxim, l)
        
        return maxim

        

if __name__ == '__main__':
    s = Solution()
    print(s.findLengthOfLCIS([1,3,5,4,7]))