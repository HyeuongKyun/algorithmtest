# N,X = map(int,input().split(' '))
# arr = list(map(int,input().split(' ')))
# list=[]
# for i in range(N):
#     if arr[i] < X:
#         list.append(arr[i])
# print(*map(int,list))


N, X = map(int, input().split())
print(*[a for a in input().split() if int(a)<X])