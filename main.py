a = 1000  # 양의 정수
print(a)

a = -7  # 음의 정수
print(a)

a = 0  #
print(a)

a = 777
print(a)

a = a + 5

############실수형

# 양의 실수
a = 157.93
print(a)

#음의 실수
a = -1837.2
print(a)

#소수부가 0일 때 0을 생략
a = 5.
print(a)
#정수부가 0일 때 0을 생략
a = -.7
print(a)

# 1,000,000,000 10억 지수 표현 방식
a = 1e9
print(a)

#752.5
a = 75.25e1
print(a)

a = int(1e9)
# 지수표현은 실수형으로 표현되기 때문에 정수로 바꾸려면 int 로 변환해줘야 함
print(a)

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

a = 7
b = 3
#나누기
print(a / b)
#나머지
print(a % b)
#몫
print(a // b)

#######################################리스트 자료형
#####################리스트 만들기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
#인덱스 4, 즉 다섯 번째 원소에 접근
print(a[4])
# 빈 리스트 선언 방법 1)
a = list()
print(a)
# 빈 리스트 선언 방법 2)
a = []
print(a)

#크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#뒤에서 첫 번째 원소출력
#뒤에서 세 번째 원소출력
#네 번째 원소 값 변경
print(a[-1])
print(a[-3])
a[3] = 7
print(a[3])

#####################리스트의 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#두 번째 원소부터 네 번째 원소까지
print(a[1:4])

#####################리스트 컴프리헨션
#0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
# i가 0부터 10번째 까지 리스트로 담김
print(array)

#0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]  # if문 먼저 작성
print(array)

#1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(10)]
print(array)

#언더바(_)의 역할 : 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용
summary = 0
for i in range(1, 10):
    summary += i
print(summary)

for _ in range(5):
    print("Hello world")

# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
#n(행)번 반복될 때 마다 m(렬)이 초기화
#길이가 m 인 list가 n번 초기화
print(array)
array[1][1] = 5
print(array)

# N X M 크기의 2차원 리스트 초기화 (잘못된 반복)
n = 4
m = 3
array = [[0] * m] * n
print(array)
array[1][1] = 5
print(array)

#####################리스트 관련 기타 메서트
a = [1, 4, 3]
print("기본 리스트:", a)

#리스트에 원소 삽입
a.append(2)
print("2삽입:", a)

#리스트 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

#특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가", a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

#리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]
#remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

#######################################문자열 자료형 p426

data = 'Hello World'
print(data)
data = "Don't you know \"Python\"?"
print(data)

#####################문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a * 3)

a = "ABCDEF"
print(a[2:4])

#######################################튜플 자료형 p427
a = (1, 2, 3, 4)
print(a)
#a[2] = 7  # 값 변경 불가능

#######################################사전 자료형 p428
##사전 자료형은 키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형
##앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비
##사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 '변경 #불가능한#(Immutable) 자료형'을 키로 사용할 수 있다
#파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 #데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
print(data)

if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다")

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
key_list = data.keys() # 키 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

#각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])


#######################################집합 자료형
#####################집합 자료형 소개 p430
#집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)
#집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)
#집합 자료형의 연산
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print(a|b) #합집합
print(a&b) #교집합
print(a-b) #차집합
#####################집합 자료형 관련 함수
data = set([1,2,3])
print(data)

#새로운 원소 추가
data.add(4)
print(data)
#새로운 원소 여러 개 추가
data.update([5,6])
print(data)

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)













