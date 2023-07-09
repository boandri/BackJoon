# 1271 엄청난부자2
# n, m = map(float, input().split())
# print(n//m)
# print(n%m)



#1330 두 수 비교하기
# A, B = map(int, input().split())
# if(A>B):
#     print('>')
# elif(A<B):
# 	print('<')
# elif(A==B):
# 	print('==')



#1809 moo
# "(___)
# (o o)____/
#  @@      \\
#   \\ ____,/
#   //   //
#  ^^   ^^"



#2338 긴자리계산
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))

# def cal(a, b):
#     print(a+b)
#     print(a-b)
#     print(a*b)

# cal(a,b)



#2420 사파리월드
# a, b = map(int, input().split())
# print(abs(a-b))



#2438 별찍기
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

#더 직관적인 방법:
# n = int(input())
# for i in range(1, n+1):
#     print("*" * i)



#2475 검증수
# a, b ,c, d, e = map(int, input().split())
# p = pow(a, 2) + pow(b, 2) + pow(c, 2) + pow(d, 2) + pow(e, 2)
# r = p % 10
# print(r)

#혹은 더 짧은 코드:
r = 0
for i in map(int, input().split()):
    r += i**2
print(r % 10)