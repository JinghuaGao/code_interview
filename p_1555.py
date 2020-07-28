class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=[1]
        for i in c:
            if len(c)<1200:
                i1=i*2
                i3=i*3
                i5=i*5
                c.append(i1)
                c.append(i3)
                c.append(i5)
                c=list(set(c))
        c.sort()
        return(c[n])

a=Solution()
a.nthUglyNumber(10)
            