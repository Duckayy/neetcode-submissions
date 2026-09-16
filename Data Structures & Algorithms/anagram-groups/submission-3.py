class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Iterate through array and for each word assign it a count of char that will act as a key and then group words with the same key
        ans = defaultdict(list)
        for word in strs:
            count_nums = [0] * 26
            for c in word:
                count_nums[ord(c) - ord('a')] += 1
            ans[tuple(count_nums)].append(word)
        return list(ans.values())