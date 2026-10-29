class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum())
        print("".join(reversed(clean.split())).lower())
        print("".join(clean.split()).lower())
        return "".join(clean.split()).lower()[::-1] == "".join(clean.split()).lower()