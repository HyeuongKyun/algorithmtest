A,B = map(int,input().split())

min = int(input())

print((A+(B+min)//60)%24,(B+min)%60)
