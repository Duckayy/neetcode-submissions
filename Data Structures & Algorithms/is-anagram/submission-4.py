class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort string and return output of if s == t
        if (len(s) != len(t)):
            return False
        return sorted(s) == sorted(t)
