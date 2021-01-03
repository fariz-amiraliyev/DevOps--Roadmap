Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength


or

def f_l(s):
    dd={}
    strt=0
    longest=0
    current_len=0

    for i,v in enumerate(s):
        if v in dd and dd[v] > strt:
            strt=dd[v] + 1
            current_len = i - dd[v]
            dd[v]=i
        else:
            dd[v]=i
            current_len+=1
            if current_len > longest:
                longest=current_len
    return longest
            
