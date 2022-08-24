class Solution:
    def twoSum(nums, target):
        hashMap = dict()#Use a dictionary as a hashmap
        for ind, ele in enumerate(nums):#Use enumerate to find the value and it's index
            difference = target-ele#Find the value that when added to the current element will sum up to the target
            #If that element exists in the Hashmap, that means we have already encountered it and added it to the hashMap
            #And in this case we can print the previously encountered value and it's index, 
            # and the current element's value and index
            if (difference in hashMap):
                return [hashMap[difference],ind]
            #If the element has not been encountered before then add it to the Hashmap along with it's index
            hashMap[ele]=ind

print(Solution.twoSum(nums = [2,7,11,15], target = 9))
print(Solution.twoSum(nums = [3,2,4], target = 6))
print(Solution.twoSum(nums = [3,3], target = 6))