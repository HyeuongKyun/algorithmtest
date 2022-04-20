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


sum = int(Math_Exp[0])
print(eval(Math_Exp[0:3]))
for i in range(N-2):
  if Math_Exp[2*i+1] == '-' and Math_Exp[2*i+3] == '-':
    Math_Exp[2*i+2] = eval(Math_Exp[2*i+2:2*i+5])
    Math_Exp = Math_Exp[:2*i+2+1]+ Math_Exp[2*i+5:]
    N = N-2

#for i in range(0,N-2):
#  Math_Exp[i+2] = op(int(Math_Exp[i]),Math_Exp[i+1],int(Math_Exp[i+2]))

print(Math_Exp[N-1])
