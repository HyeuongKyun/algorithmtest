a,b = map(int,input().split(' '))
if a<b:
    print('<')
elif a>b:
    print('>')
else:
    print('==')

# a,b=map(int,input().split())
# print(("<>"[a>b],"==")[a==b])