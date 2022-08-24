class Solution:
    def checkSameTypeBracket(s1: str, s2: str)->bool:
        #This function is used to check if the opening brace added to the stack 
        # has a corresponding closing brace that is read in the string
        if(s1=='(' and s2==')'):
            return True
        if(s1=='{' and s2=='}'):
            return True
        if(s1=='[' and s2==']'):
            return True
        return False #This means the stack top and the processed character are not opening and closing brace, so we return False
        
    def isValid(s: str) -> bool:
        charstack = []#Use a Python list as a stack
        for char_val in s:
            if(len(charstack)==0):
                #When the stack is empty add the encountered symbol to the stack
                charstack.append(char_val)
            elif(Solution.checkSameTypeBracket(charstack[-1], char_val)):
                #When the encountered symbol is the closing brace for the stack top opening brace character then pop it form stack
                charstack.pop()
            else:
                #When the encountered symbol is not the closing brace for the stack top opening brace character, or
                # the stack closing character is at the top then add the new character encountered to the stack top
                charstack.append(char_val)
        if(len(charstack)>0):
            return False
        else:
            return True
            
            
print(Solution.isValid("()"))
print(Solution.isValid("()[]{}"))
print(Solution.isValid("(]"))

        