"""
해시
해시란 데이터를 다루는 기법 중에 하나며, 검색과 저장이 아주 빠르게 진행됩니다.
빠르게 진행이 되는 이유는 데이터를 검색할 때 사용할 key와 실제 데이터 값이 한 쌍으로 존재하고,
key 값이 배열의 인덱스로 변환되기 때문입니다.
- 데이터를 다루는 기법 중 하나로 검색과 저장이 아주 유용한 구조
key와 value 쌍으로 데이터를 저장
"""

"""
key - 해시 함수 - value
해시 함수란
- 임의의 길이를 갖는 메세지를 입력 받아 고정된 길이의 해시값을 출력하는 함수
함수 hash()
"""
hash(12.34)

"""
해시 구현 방법
- 딕셔너리 사용
"""

# 닥셔너리 삽입
hash = {}
hash = dict()

hash[1] = 'apple'
hash['banana'] = 3
hash[(4, 5)] = [1, 2, 3]
hash[10] = dict({1: 'a', 2: 'b'})
# hash[[1, 2, 3]] = 5
# hash[{1, 2, 3}] = 'orange'
""" 집합과 리스트는 사용이 불가능 """

hash

"""
딕셔너리 수정
"""
hash[1] = 'melon'
hash['banana'] = 10

hash

"""
딕셔너리 값 추출
"""
hash.pop(1)

hash.pop('banana')

hash.pop((4, 5))

hash.pop(10)

hash

hash = {}
hash = dict()

hash[1] = 'apple'
hash['banana'] = 3
hash[(4, 5)] = [1, 2, 3]
hash[10] = dict({1: 'a', 2: 'b'})

"""
딕셔너리 삭제
"""
del hash[1]
del hash['banana']
del hash[(4, 5)]
del hash[10]

hash

"""
딕셔너리 루프
"""
hash = dict()
hash.keys()  # key 추출
hash.values()  # value 추출
hash.values()  # key와 value 추출

"""
닥셔너리 루프
"""
hash = dict()
for i in range(1, 6):
    hash[i] = i ** 2

for k in hash.keys():
    print(k)

for v in hash.values():
    print(v)

for k, v in hash.items():
    print(k, v)

"""
딕셔너리 정렬
sorted() - 언제나 list 타입으로 반환
"""

"""오름 차순 정렬
"""
hash = dict({1: 10, 3: 12, 5: 7, 7: 6, 4: 5})
sorted(hash.keys(), key=lambda x: x)

sorted(hash.values(), key=lambda x: x)

sorted(hash.items(), key=lambda x: x)
# keys, values 정렬

"""
내림차순 정렬
"""

sorted(hash.keys(), key=lambda x: -x)

sorted(hash.values(), key=lambda x: -x)

sorted(hash.items(), key=lambda x: -x)
"""
하지만 error 발생 
튜플 형식으로 반환 하는것이라 - 마이너스 값을 정렬할 수 없다
"""

sorted(hash.items(), key=lambda x: -x[1])
# 정상적으로 내림차순 정렬
# x[0] key, x[1] value
# x[1] value , x[0]key
