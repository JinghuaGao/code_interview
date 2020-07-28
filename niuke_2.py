x,y=map(int,raw_input().split())
s=map(int,raw_input().split())
for i in range(y):
    a,b,c=map(str,raw_input().split())
    b=int(b)
    c=int(c)
    if a=='Q':
        t=max(s[b-1:c])
        print t
    else:
            s[b-1]=c