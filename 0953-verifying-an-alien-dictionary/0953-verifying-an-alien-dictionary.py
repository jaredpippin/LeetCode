class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True
        
        dictHashTable = {}
        for i, char in enumerate(order):
            dictHashTable[char] = i
        
        def stringComp(str1: str, str2: str) -> bool:
            i = 0
            while (i<len(str1) and i<len(str2)):
                order1 = dictHashTable[str1[i]]
                order2 = dictHashTable[str2[i]]
                i += 1
                if (order1 > order2):
                    return False
                elif (order1 < order2):
                    return True
            if i < len(str1):
                return False
            
            return True
        
        for i in range(len(words) - 1):
            if not stringComp(words[i], words[i+1]):
                return False
        return True