A string S of lowercase English letters is given. We want to partition this
string into as many parts as possible so that each letter appears in at most
one part, and return a list of integers representing the size of these parts.





Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.



class Solution(object):
		def partitionLabels(self, S):
			"""
			:type S: str
			:rtype: List[int]
			"""

			lengths = []
			dic = {}

			for i in range(len(S)):
				dic[S[i]] = i
			# Find last occurence of word in string
			i, count, words = 0, 0, set()
			while i < len(S):

				if i != dic[S[i]] and S[i] not in words:
					words.add(S[i])

				if i == dic[S[i]]:
					words.discard(S[i])
					# discard is similar to remove but if element
					# does not exist in set, it does not return error
				count += 1


				if len(words) == 0:
					lengths.append(count)
					count = 0
					words = set()

				i += 1

			return lengths
