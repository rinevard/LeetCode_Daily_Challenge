# 2023/11/13 Daily challenge
# https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_ls = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        vowel_set = set(vowel_ls)
        vowels = {i: 0 for i in vowel_ls}
        vowel_idx = []
        ans_ls = [None] * len(s)

        for i in range(len(s)):
            # the vowels must be sorted, therefore we can store ord(char) in the list.
            if s[i] in vowel_set:
                vowels[s[i]] += 1
                vowel_idx.append(i)
            else:
                ans_ls[i] = s[i]

        # put the vowels back to the ans according to the previously sorted vowel_ls and the count of each vowel
        vowel_idx = iter(vowel_idx)
        for c in vowel_ls:
            for _ in range(vowels[c]):
                ans_ls[next(vowel_idx)] = c
        
        # make the list into string
        ans = ''.join(ans_ls)
        return ans