class Solution:
    def search(nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid =low+(high-low)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return -1
print(Solution.search(nums = [-1,0,3,5,9,12], target = 9))
print(Solution.search(nums = [-1,0,3,5,9,12], target = 2))