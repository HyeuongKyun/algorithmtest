n,m = map(int,input().split())

s=[]

def dsf(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        s.append(i)
        dsf(i)
        s.pop()
        
dsf(1)