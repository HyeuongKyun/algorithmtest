H,M = map(int,input().split())

# if M-45>=0:
#     print(H,M-45)
# elif M-45<0 and H-1>=0:
#     print(H-1,M+15)
# else:
#     print(23,M+15)


# if M-45<0:
#     H = H-1
#     M = M-45+60
#     if H-1<0:
#         print(H+24,M)
#     else:
#         print(H,M)
# else:
#     print(H,M-45)
#왜 틀린지 이해 안감



print((H-(M<45))%24,(M-45)%60)



