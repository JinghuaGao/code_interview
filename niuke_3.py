a,b=raw_input()
c=min(a,b)
d=max(a,b)

ans=[]
for i in range(2,c+1):
    if c%i==0 and d%i==0:
        ans.append(i)

if len(ans)>0:
    print a*b/max(ans)
else:
        print a*b