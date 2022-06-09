# try:
#     while True:
#         A, B = map(int, input().split())
#         print(A+B)
# except:
#     print("error")  틀림
    
    
#이게 맞음. 뭐지.?
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break