def lengthOfLastWord(self, s: str) -> int:
        return 0 if not s.strip() else len(s.split()[-1])
