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
# r = 0
# for i in map(int, input().split()):
#     r += i**2
# print(r % 10)



#2558 A+B
# a = int(input())
# b = int(input())
# print(a+b)



#2739 구구단
# a = int(input())
# result = 0
# for i in range(1, 10):
#     print(f"{a} * {i} = {(a * i)}")



#2741 N찍기
# a = int(input())
# for i in range(1, a+1):
#     print(i)



#2743 단어 길이 재기
# a = input()
# print(len(a))



#2744 대소문자 바꾸기
# a = input()
# print(a.swapcase)



#2753 윤년
# i = int(input())
# if((i % 4) == 0):
#     if((i % 100) != 0 ) or ((i % 400) == 0):
#         print("1")
#     else:
#         print('0')
# else:
#     print('0')



#2754 학점계산
# grade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0}
# print(grade[input()])



#3003 킹, 퀸, 룩, 비숍, 나이트, 폰
num_of_pieces = [1, 1, 2, 2, 2, 8]
inp = list(map(int, input().split()))
for i in range(6):
    print(num_of_pieces[i]-inp[i], end=" ")