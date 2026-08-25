class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        outputs = [0] * (len(s))
        n = len(s)
        for index in range(n):
        #keeps giving array length because comparing 2 strings
            char1 = s[index:index:]
            char2 = s[index+1:index+1:]
            print(char1, char2)
            print("test")
            if char1 == char2:
                outputs[index] = output
                output = 0
            else:
                output += 1
            index += 1
        