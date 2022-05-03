n,m = map(int, input().split())

s=[]

def recur(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return 
    
    for i in range(start,n+1):
        s.append(i)
        recur(i+1)
        s.pop()
            
recur(1)








# =============================================================================
#         if i > s[i-1]:  
#             s.append(i)
#             recur()
#             s.pop()
#     for i in range(1,n+1):
#             
# =============================================================================
