 def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return t

        mem = dict()

		# remember the occurrence of every char in s
        for char in s:
            if char not in mem:
                mem[char] = 1

            else:
                mem[char] += 1

        # the char with wrong occurrence is the newly added char
        for char in t:
            if char in mem:
                if mem[char] > 0:
                    mem[char] -= 1
                else:
                    return char

            else:
                return char
