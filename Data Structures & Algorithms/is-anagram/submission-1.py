class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Use counter and return check based on if counter of each string equals
        return Counter(s) == Counter(t)
        