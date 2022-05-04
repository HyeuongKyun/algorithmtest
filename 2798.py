n, m = map(int,input().split())

# 3<=n<=100 , 10<=M<=300,000

card = list(map(int,input().split()))

s = 0
Hap = []
maxi=0

def recur(start):
    global maxi
    
    if len(Hap)==3:
        s = Hap[0] + Hap[1] + Hap[2]
        if (s <= m) and (maxi < s):
            maxi=s
            
        return 
    
    for i in range(start,n):
        if card[i] not in Hap:
            Hap.append(card[i])
            recur(i)
            Hap.pop()
    return

recur(0)                 
print(maxi)


# =============================================================================
#chad9349님의 풀이 
# def GetMaxBlackJackNumbers(N, M, nums):
# 	sums = set()
# 	for i in range(N-2):
# 		for j in range(i+1, N-1):
# 			for k in range(j+1, N):
# 				sum = nums[i] + nums[j] + nums[k]
# 				if sum <= M:
# 					sums.add(sum)
# 					break
# 
# 	return max([*sums])
# 
# N, M = map(int, input().split())
# nums = sorted(list(map(int, input().split())), reverse=True)
# print(GetMaxBlackJackNumbers(N, M, nums))
# 
#
#  for문을 통해서 
#
#
#
# 새롭게 알게된 문법 sorted와 sorted의 속성 reverse=True
#
# sort와 sorted의 기능은 둘 다 정렬을하는 것인데 sort는 리스트만 가능하고, 
# sorted는 리스트와 문자열 둘 다 가능하다. 
#
#
#a = ['a','c','b','d']
#a.sort()
#print(a)
#['a','b','c','d']
#
#a = ['a','c','b','d']
#a = sorted(a)
#print(a)
#['a','b','c','d']
#
#위와 같은 방법으로 사용이되고 sorted는 정렬 결과를 리턴하기 때문에 변수에 담을 수 있고 
#sort는 리턴이 없고 입력을 출력이 덮어쓴다. 변수에 담을 수도 없다. 
#
#그리고 sort와 sorted 둘다 그냥 사용하면 오름차순 정렬인데 reverse=True를 사용하면 내림차순 정렬이 된다.
# =============================================================================








