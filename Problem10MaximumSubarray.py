class Solution:
    def maxSubArray(nums: list[int]) -> int:
        maxRes = nums[0]
        curr_sum = 0
        for n in nums:
            if (curr_sum<0):
                curr_sum=0
            curr_sum+=n
            maxRes = max(curr_sum, maxRes)
        return maxRes


print(Solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(Solution.maxSubArray(nums = [1]))
print(Solution.maxSubArray(nums = [5,4,-1,7,8]))