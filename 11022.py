T=int(input())
A=[]
B=[]

for i in range(1,T+1):
    a,b=map(int,input().split(' '))
    A.append(a)
    B.append(b)
for i in range(T):
    print('Case #%d: %d + %d = %d'%(i+1,A[i],B[i],A[i]+B[i]))