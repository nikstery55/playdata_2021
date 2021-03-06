"""
진법변환/ 비트연산
"""

"""진법 이란
수를 셀 때 자릿수가 올라가는 단위를 기준으로 하는 셈법의 총칭
사용하는 숫자의 개수가 진법의 숫자를 의미
"""

"""10진법 -> 2진법

10을 2로 나누면 --- 나머지는 0 
5를 2로 나누면 --- 나머지는 1
2를 2로 나누면 --- 나머지는 0
1
10을 이진법으로 하면 1010(2)가 됨
"""


"""
함수로 이진법으로 바꾸는 방법
bin 함수
0b의 뜻은 2진법을 의미하는 binary의 약자
"""
bin(10)

"""
10진법 -> 8진법
95를 8로 나누면 --- 나머지는 7
11을 8로 나누면 --- 나머지는 3
1
95를 8진법으로 하면 127(8)가 됨
"""

"""
함수로 8진법으로 바꾸는 방법
oct함수
0o의 뜻은 8진법을 의미함
"""
oct(95)

"""
10진법 -> 16진법 
대신 10이후의 명명법은
10-> a 
11-> b
12-> c
13-> d
14-> e
15-> f
"""

"""
10진법 -> 16진법
350을 16으로 나누면 --- 나머지 e(14)
21을 16으로 나누면 --- 나머지 5
1
350을 16진법으로 하면 15e(16)가 됨
"""

"""
함수로 16진법을 바꾸는 방법
hex 함수
0x의 뜻은 16진법을 의미함
"""
hex(350)

"""
함수로 n진법 -> 10진법 바꾸는 방법
int() 함수로 바꾼다
"""
int(0b1101)

int(0o73)

int(0x7e)

"""
비트연산
한개 혹은 두개의 이진수에 적용되는 연산
"""

"""
비트연산 종류
&     |   ^     ~  <<,>>
AND, OR, XOR, NOT, SHIFT

AND - 각각의 자릿수를 비교하여 둘다 1일 경우1, 아니면 0을 반환
OR - 각각의 자릿수를 비교하여 둘 중 하나가 1일 경우1, 아니면 0을 반환
XOR - 각각의 자릿수를 비교하여 다르면 1, 같으면 0을 반환
NOT - 비트 반전 연산자로 1은 0 으로 0은 1로 변환 (비트 연산에 대한 2진수의 음수) 음수의 표현을 처리하기 위함 - 1을 더한 뒤 부호를 바꿔준다
SHIFT - << 비트 이동 연산자로 왼쪽으로 주어진 수만큼 옮긴다, >> 비트 이동 연산자로 오른쪽 주어진 수만큼 옮긴다
"""

"""
비트연산 활용
1. 컴퓨터 연산을 위한 비트 필드
2. 데이터의 압축 및 암호화
3. 유한 상태 기계
4. 컴퓨터 통신을 위한 포트 및 소켓
"""
