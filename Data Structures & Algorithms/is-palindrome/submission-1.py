class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum())
        return "".join(clean.split()).lower()[::-1] == "".join(clean.split()).lower()