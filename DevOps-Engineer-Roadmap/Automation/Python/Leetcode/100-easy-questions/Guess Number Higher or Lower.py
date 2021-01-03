class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        begin=1
        end=n
        middle=(begin+end)/2
        while end>=begin:
            if guess(middle)==0: return middle
            if guess(middle)==-1:
                end=middle-1
                middle=(begin+end)/2
            if guess(middle)==1:
                begin=middle+1
                middle=(begin+end)/2

        return middle;
