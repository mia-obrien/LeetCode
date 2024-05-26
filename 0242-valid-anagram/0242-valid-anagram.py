class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(Counter(s)== Counter(t)): #if(sorted(s)== sorted(t)): Counter is fasterthan sorted
            return True
        else:
            return False