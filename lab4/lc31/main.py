class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i, idx = len(nums)-1, -1
        while i >= 1:
            if nums[i-1] < nums[i]:
                idx = i-1
                break
            i-=1
        
        if idx == -1:
            nums.reverse()
            return

        nums[idx+1:] = nums[len(nums)-1:idx:-1]

        j = -1
        for i in range(idx+1, len(nums)):
            if nums[idx] < nums[i]:
                j = i
                break

        nums[idx], nums[j] = nums[j], nums[idx]

s = Solution()

l = [3, 2, 1]
s.nextPermutation(l)

print(l)