class Solution:
    def maxProfit(prices: list[int]) -> int:
        #Solve using two pointers
        lftptr = 0
        rhtptr = 1
        maxprofit = 0
        while(rhtptr<len(prices)):#If the right pointer exceeds the length of the prices list stop
            profit = prices[rhtptr]-prices[lftptr]
            if(profit>0):
                maxprofit = max(profit, maxprofit) #If the prices list element at right pointer is greater than left pointer it
                #means there is a profit, so we find the maximum of this profit and the maxprofit which is initially set to 0
            else:
                lftptr=rhtptr#Else move the left pointer to the right pointer
            rhtptr+=1#Increment the right pointer at each step
        return maxprofit #Return the maxprofit outside the loop
            
print(Solution.maxProfit(prices = [7,1,5,3,6,4]))
print(Solution.maxProfit(prices = [7,6,4,3,1]))