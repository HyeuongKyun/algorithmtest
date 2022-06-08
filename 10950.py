# n=int(input())
# A=[]
# B=[]
# for i in range(n):
#     a,b=map(int,input().split(' '))
#     A.append(a)
#     B.append(b)
# for i in range(n):
#     print("%d"%(A[i]+B[i]))

for i in range(int(input())):
    print(sum(map(int,input().split())))
#이렇게 되면 하나씩 출력이 되긴하지만 뭐 그냥그렇네