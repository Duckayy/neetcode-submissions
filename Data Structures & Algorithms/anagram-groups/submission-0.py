class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Use counter to count num of chars in string if they equal then add to corresponding group
        result = defaultdict(list) #creates list for grouping
        for word in strs: #iterates through word
            count = [0] * 26 #creates a id counter that we will use to track characters in word
            for c in word: #iterates through characters in word
                count[ord(c) - ord('a')] += 1 #increments count of character at the appropriate index by subtract a to have proper index position
            result[tuple(count)].append(word) #appends word at tuple where count is equal to word count
        return list(result.values()) #returns the values located at the tuple
