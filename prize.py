
n,m = map(int, input().split())

graph = []
# graph1 = []
result = 0
# reult = 0

for i in range(n):
    graph.append(list(map(int,input())))
    # graph1.append(list(map(int,input())))


def dfs(x,y):
    print(x,y)
    if x <= -1 or x >=n or y <=-1 or y >= m:
        print("False1")
        return False
    else:
        print("pass1")
    
    if graph[x][y] == 0:
        graph[x][y] =1
       
        dfs(x-1 ,y)
        dfs(x ,y-1)
        dfs(x+1 ,y)
        dfs(x ,y+1)
        print("True")
        return True
    else:
        print("passTrue")
    print("False2")
    return False


for i in range(n):
    for j in range(m):
        
        if dfs(i, j) == True:
            print("eeeeeeeend",i,j)
            result += 1
            
# =============================================================================
#             
# for a in range(n):
#     for b in range(m):
#         print(dfs(a,b,graph1))
#         
# =============================================================================
print(result)


# =============================================================================
# a=list(input())
# print(type(a))
# print(a)
# 
# =============================================================================
