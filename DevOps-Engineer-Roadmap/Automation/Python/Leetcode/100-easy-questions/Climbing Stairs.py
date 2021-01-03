def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ct=[0]*(n+1)
        ct[0]=ct[1]=1

        for i in range(2,n+1):
            ct[i]= ct[i-1]+ct[i-2]
        return ct[n]
