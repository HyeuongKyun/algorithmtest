num_of_seq=int(input())
number = list(map(int,input().split()))
plus,minus,mul,spli=map(int,input().split())
# oper=['+','-','*','//']
oper=[]

for i in range(plus):
    oper.append('+')
for i in range(minus):
    oper.append('-')
for i in range(mul):
    oper.append('*')
for i in range(spli):
    oper.append('//')
print(oper)

realoper=[]
realoperi=[]

def dsf():
    if len(realoperi)==num_of_seq-1:
        # print(' '.join(map(str,realoperi)))
        for i in range(num_of_seq-1):
            number.insert(0,eval(str(number.pop(0))+oper[realoperi[i]]+str(number.pop(0))))
        return number[0]
    
    for i in range(0,num_of_seq-1):
        if i not in realoperi:
            realoperi.append(i)
            dsf()
            realoperi.pop()


dsf()
 # def maxmin():
 #     number.insert(0, str(number.pop(0)) + realoper.pop(0))
     
# =============================================================================
# 
# def dfs():
#     n=num_of_seq.pop(0)
#     oper.append(n)
#     oper.append
#                 
# =============================================================================
    

#number.insert(0,eval(str(number.pop(0))+oper[0]+str(number.pop(0))))

# print(number)

# =============================================================================
# print(number)
# 
# print(number.pop(0))
# print(number.pop(0))
# 
# print(oper[0])
# ===================================================================