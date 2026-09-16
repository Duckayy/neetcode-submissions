class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Step 1: Create dictionary to make unique hashable elements
        #Step 2: Iterate through each word and create an array to count each instance of char
        #Step 3: For each word iterate through each character and increment its place in array count 
        #Step 4: Append word along with its array count whcih count will act as key for group of anagram
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())