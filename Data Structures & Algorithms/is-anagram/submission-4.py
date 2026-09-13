class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hash = {} # on solo un hashmap, sumamos en la iteracion de s y restamos en la iteracion de t
        for i in s:
            hash[i] = hash.get(i,0) + 1
        for i in t: 
            hash[i] = hash.get(i,0) - 1


        for count in hash.values(): # iteramos en los valores 
            if count != 0:
                return False
        return True
