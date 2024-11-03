class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        i, j = 0, 0
        ans = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])
                j+=1

        while i < m:
            ans.append(nums1[i])
            i+=1
        
        while j < n:
            ans.append(nums2[j])
            j+=1

        for i in range(n+m):
            nums1[i] = ans[i]
        print(nums1)
            

if __name__ == '__main__':
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        