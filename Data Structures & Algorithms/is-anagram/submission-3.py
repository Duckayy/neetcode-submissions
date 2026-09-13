class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort string and return output of if s == t
        return sorted(s) == sorted(t)
