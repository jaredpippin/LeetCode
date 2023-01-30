class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:   
        d1={}
        d2={}
        count=0
        if len(pattern)!=s.count(' ')+1: #wrong length
	        return False
    
        for i in s.split(): #check each member of s
            if i not in d1: #not in d1
                d1[i]=pattern[count] #set d1
            else:
                if d1[i]!=pattern[count]: #not equal to where it should be in d1
                    return False
            if pattern[count] not in d2: #not in d2
                d2[pattern[count]]=i  #set d2
            else:
                if d2[pattern[count]]!=i: #not equal to where it should be in d2
                    return False
            count+=1 #count up
        return True