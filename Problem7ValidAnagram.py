class Solution:
    def isAnagram(s: str, t: str) -> bool:
        if(sorted(s)==sorted(t)):
            return True
        return False
    
print(Solution.isAnagram(s = "anagram", t = "nagaram"))
print(Solution.isAnagram(s = "rat", t = "car"))

        