class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        n=2.0
        c=[]
        while n<(2*target)**0.5:
            if n%2==0 and target/n-int(target/n)==0.5:
                c.append([int(target/n)-int(n/2)+1+i for i in range(int(n))])
            if n%2==1 and target/n-int(target/n)==0:
                c.append([int(target/n)-int(n/2)+i for i in range(int(n))])
            n+=1
        c.reverse()
        print c
        
a=Solution()
a.findContinuousSequence(9)