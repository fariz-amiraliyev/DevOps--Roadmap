Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(char for char in s if char.isalnum())
        i = 0
        j = len(s)-1
        while j>i:
            if s[i].lower() != s[j].lower():
                return False
            j -= 1
            i += 1

        return True
