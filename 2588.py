num = int(input())
num2 = int(input())
A = num2//100
B = (num2-A*100)//10
C = (num2-A*100-B*10)//1

print(num*C);
print(num*B);
print(num*A);
print(num*C+ num*B*10 + num*A*100);


# a,b=map(int,open(0))
# print(b%10*a,b%100//10*a,b//100*a,b*a)