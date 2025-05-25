class Solution(object):
    def longestPalindrome(self, words):
        n, ans = len(words), 0
        words_dict = dict()
        for i in range(n):
            word = words[i]
            backword = word[1]+word[0]
            if backword in words_dict:
                words_dict[backword] -= 1
                if words_dict[backword] == 0:
                    del words_dict[backword]
                ans += 4
                continue
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        for key in words_dict:
            if key[0] == key[1]:
                ans += 2
                break
        return ans
