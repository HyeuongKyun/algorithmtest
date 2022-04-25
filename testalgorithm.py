

#def op(a,strOperator,b):
#  if strOperator == '*':
#    return a*b
#  if strOperator == '+':
#    return a+b
#  if strOperator == '-':
#    return a-b


while True:
  try:
    N = int(input("수식의 길이를 입력하세요.(연산자 포함, 수식의 길이는 0<N<20입니다.) :"))
    if N>19 or N<1:
      N/0
  except:
    print("입력이 옳바르지 않습니다.")
  if N <20 and N > 0:
    break


while True:
  Math_Exp = input("수식을 입력하세요. : ")

  try:
    if not isinstance(Math_Exp, str):
      N/0
    if len(Math_Exp) != N:
      N/0
  except:
    print('수식이 올바르지 않습니다.')
  if isinstance(Math_Exp, str) and len(Math_Exp) == N:
    break




# for i in range(N-3):
#   if Math_Exp[i] == '-' and Math_Exp[i+2] == '-':
#     if eval(Math_Exp[i+1:i+4]) < 0:
#         Math_Exp = Math_Exp[:i] + '+' + str(abs(eval(Math_Exp[i+1:i+4]))) + '+0' + Math_Exp[i+4:]
#     else:
#         Math_Exp = Math_Exp[:i+1] + str(eval(Math_Exp[i+1:i+4])) + '+0' + Math_Exp[i+4:]

# print(Math_Exp)

# =============================================================================
# 
# # Math_Exp = Math_Exp[:1] + str(eval(Math_Exp[0:3])) + Math_Exp[3:]
# print(Math_Exp)
# # Math_Exp = Math_Exp[:4] + str(eval(Math_Exp[1:5])) + Math_Exp[5:]
# 
# result = eval(Math_Exp[0:3])
# list=[]
# for i in range(2,N-2,2):
#     result = eval(str(result) + Math_Exp[i+2:i+3])
#     print(result)
# 
# print(result)
# =============================================================================


Math_Exp = Math_Exp[:1]+str(eval(Math_Exp[:3]))+Math_Exp[4:]
for i in range(2,N-2,2):
    if (eval(Math_Exp[i:i+3]) < 0 and Math_Exp[i-1] == '-') or (eval(Math_Exp[i:i+3]) > 0 and Math_Exp[i-1] == '+'):
        Math_Exp = Math_Exp[:i+1] + '+' + str(abs(eval(Math_Exp[i:i+3]))) + Math_Exp[i+3:]
    else: #(eval(Math_Exp[i:i+3]) > 0 and Math_Exp[i-1] == '-') or  eval(Math_Exp[i:i+3]) < 0 and Math_Exp[i-1] == '+':
        Math_Exp = Math_Exp[:i+1] + '-' + str(eval(Math_Exp[i:i+3])) + Math_Exp[i+3:]
    print(Math_Exp)

# print(Math_Exp[len(Math_Exp)-1])









# =============================================================================
# 
# arr = '2-5-8'
# my_arr = arr.split()
# my_arr.insert(1,'+')
# print(my_arr)
# # arr[5]='+'
# # print(arr)
# # print(isinstance(arr[1], str))
# =============================================================================





















