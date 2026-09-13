class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Sort strings then check if they equal
        return sorted(s) == sorted(t)