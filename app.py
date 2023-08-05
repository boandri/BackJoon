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
# num_of_pieces = [1, 1, 2, 2, 2, 8]
# inp = list(map(int, input().split()))
# for i in range(6):
#     print(num_of_pieces[i]-inp[i], end=" ")



#4101 크냐?
# a, b = map(int, input().split())
# while True:
#     if(a == 0) and (b == 0):
#         break
#     elif(a > b):
#         print("Yes")
#         a, b = map(int, input().split())
#     else:
#         print("No")
#         a, b = map(int, input().split())


#4999 아!
# jay =  input()
# doc = input()
# # if(len(jay) >= len(doc)):
# #     print('go')
# # else:
# #     print('no')
# print('go' if len(jay) >= len(doc) else "no")



# #5337 welcome
# print('.  .   .')
# print('|  | _ | _. _ ._ _  _')
# print('|/\|(/.|(_.(_)[ | )(/.')



#5338 microsoft logo
# print("""       _.-;;-._
# '-..-'|   ||   |
# '-..-'|_.-;;-._|
# '-..-'|   ||   |
# '-..-'|_.-''-._|""")



# #5522 card game
# r = 0
# for i in range(5):
#     r += int(input())
# print(r)



#5597 과제 안내신분?
# students = list(range(1,31))
# a = list()
# for i in range(28):
#     students.remove(int(input()))
# print(min(students))
# print(max(students))



#8393 합
# gen = list(range(1,int(input())+1))
# sum = sum(gen)
# print(sum)



#9086 문자열
# a = list()
# for i in range(int(input())):
#     a.append(input())
# for i in range(len(a)):
#     print(a[i][0]+a[i][-1])


#9498 시험성적
# score = int(input())
# if(score >= 90 and score <= 100):
#     print("A")
# elif(score >= 80 and score <=89 ):
#     print("B")
# elif(score >= 70 and score <=79 ):
#     print("C")
# elif(score >= 60 and score <=69 ):
#     print("D")
# else:
#     print("F")


#10430 나머지
# a, b, c = map(int, input().split())
# print((a+b)%c)
# print(((a%c) + (b%c))%c)
# print((a * b)%c)
# print(((a%c) * (b%c))%c)



#10718 We love kriii
# print("강한친구 어쩌고 \n상한친구 어쩌구")



#10871 X보다 작은 수
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# b = list()
# for i in range(n):
#     if(a[i]< x):
#         b.append(a[i])
# for i in range(len(b)):
#     print(b[i], end=' ')



#11654 ascii code
print(ord(input()))