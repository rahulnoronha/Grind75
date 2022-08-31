class Solution:
    def isPalindrome(s: str) -> bool:
        alnumstr = [i.lower() for i in s if i.isalnum()] #Use list comprehension to get only alphanumeric characters from the string in a list
        return(alnumstr ==alnumstr[::-1])#Check if the reverse of the list equals the list

    
print(Solution.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(Solution.isPalindrome(s = "race a car"))
print(Solution.isPalindrome(s = " "))