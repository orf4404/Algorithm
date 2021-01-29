##############################################입출력
################## 입력을 위한 전혁적인 소스코드
# 데이터 개수 입력

#n = int(input())
# 각 데이터를 공백으로 구분하여 입력
#data = input() #5명의 성적 정보
#data_split = input().split() # 공백기준으로 각각의 문자열이 나누어져 리스트 형태로 저장
#data_map = list(map(int,input().split())) #맵함수를 통해서 각각의 리스트를 정수형으로 만들어주고 리스트 형태로 만들어 줌 

#print(n)
#print(data)#문자열 리스트
#print(data_split) #정수형 리스트
#print(data_map)



#data.sort(reverse = True)
#print(data)

#n, m, k를 공백으로 구분하여 입력
#n, m, k = map(int, input().split()) #n m k의 개수와 input(입력값) 의 개수가 같아야 한다
#print(n, m, k)

#import sys
#data = sys.stdinreadline().rstrip()
#print(data)

a = 1
b = 2
print(a)# print 함수는 기본적으로 출력 이후에 줄 바꿈을 수행한다
print(b)
print(a,b)
print(7, end = " ") #end 를 넣어서 줄 바꿈이 일어나지 않게 함
print(8, end = " ")
#출력할 변수
answer = 7
print("정답은 " + str(answer) + "입니다.") 
# 정수형을 문자형으로 변경 후 출력
#파이썬에서는 변수나 상수 값을 출력하고자 할 때 print 함수 사용 

#f-string
answer = 7
print(f"정답은 {answer}입니다") # 자료형의 형변환 없이 문자열과 정수를 함께 사용 가능


