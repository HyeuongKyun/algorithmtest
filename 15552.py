import sys
n=int(sys.stdin.readline())
A = []; B = [];
for i in range(n):
    a,b=map(int,sys.stdin.readline().split(' '))
    A.append(a);
    B.append(b);
for i in range(n):
    print(A[i]+B[i]);


# for i in range(n):
#     a,b = map(int,input().split())
#     A.append(a);
#     B.append(b);
# for i in range(n):
#     print(A[i]+B[i]);