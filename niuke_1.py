#https://www.nowcoder.com/question/next?pid=260145&qid=25368&tid=34580112
#coding=utf-8 
pokers=raw_input()
p=[3,4,5,6,7,8,9,10,'J','Q','K','A',2,'joker','JOKER']
p=[str(i) for i in p]
s=pokers.index('-')
x=pokers[:s].split(' ')
y=pokers[s+1:].split(' ')
x=[p.index(i) for i in x]
y=[p.index(i) for i in y]

out=[pokers[:s],pokers[s+1:],'ERROR']

def find_type(a):
    t=len(a)
    if len(a)==2 and a[1]>13:
        t=10
    if len(a)==4:
        t=10
    return t
def comp(a,b):
    if find_type(a)==find_type(b):
        c=(b[0]>a[0])
    elif find_type(a)==10:
            c=0
    elif find_type(b)==10:
                c=1
    else:
                    c=2
    return out[int(c)]

print comp(x,y)
        
