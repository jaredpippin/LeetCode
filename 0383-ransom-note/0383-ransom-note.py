class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        
        #fill up our map with the characters of magazine and the counts of each letter
        for i in magazine:
            if i not in dict: #set number to one if first time encounter
                dict[i] = 1
            else:
                dict[i] += 1 #add one if already encountered
                
        #check what we need in ransomNote        
        for j in ransomNote:
            if j not in dict or dict[j] == 0: #if character is not found in our dict or if count is already depleted
                return False #failure to be constructed
            else:
                dict[j] -= 1
        return True #if we make it here then it is successfully constructed
            
            