# =============================================================================
# def dfs(n):
#     if n > 7:
#         return
#     else:
#         dfs(2*n)
#         print(n, end=" ")
#         dfs(2*n + 1)
#         
#         
#         
# dfs(1)
# 
# =============================================================================


n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            
            
            dfs()
            
            
            
            s.pop()
 
dfs()