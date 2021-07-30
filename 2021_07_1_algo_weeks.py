#스택
#프로그래밍에서 목록 혹은 리스트에서 접근이 한 쪽에서만 가능한 구조
# LIFO(Last-in, First-Out)가 기본원리
# 스택 함수
# push peek pop
#스택을 추가하는 함수 push
#가장 마지막에 들어간 스택을 확인하는 함수 peek
# 가장 마지막에 들어간 스택을 가져가는 함수 push
#파이썬 스택의 구현 방볍
#1. 직접구현 2. 이미 구현된 클래스 import 3.list를 스택으로 구현
#직접구현
#파이썬
class Stack(list):
    push = list.append

    def peek(self):
        return self[-1]
    # pop은 list의 내장함수로 이미 존재

s = Stack()
s.push(1)
s.push(5)
s.push(10)
print("my stack is:", s)
print("popped value is :", s.pop())
print("my stack is:", s)
print("peeked value is :", s.peek())
print("my stack is:", s)
# list를 스택으로 활용
s = [ ]
s.append(1)
s.append(5)
s.append(10)
print("my stack is :", s)
print("popped value is :", s.pop())
print("my stack is :", s)
print("peeked value is :", s[-1])
#리스트로 해서 peek이 아니라 s[-1]
print("my stack is:", s)
# 스택의 활용  , 브라우저 이전페이지 다음페이지###

#큐 queue
#일이 처리되기를 기다리는 리스트
#프로그래밍에서 목록 혹은 리스트에서 접근이 양쪽에서 가능한 구조로 FIFO(First-In, First-Out가 기본원리
#큐 함수
#put peek get
# 큐를 추가하는 함수 put
# 가장 먼저 들어간 큐를 확인하는 함수 peek
# 가장 먼저 들어간 큐를 가져가는 함수 get
#큐의 구현 방밥
# 1. 직접 구현 2. 이미 구현된 클래스 import  3 list를 큐로 구현
# 큐 직접 구현
class Queue(list):
    put = list.append

    def peek(self):
        return self[0]

    def get(self):
        return self.pop(0)

q = Queue()
q.put(1)
q.put(5)
q.put(10)
print("my queue is :", q)
print("removved value is :", q.get())
print("my queue is:", q)
print("peeked value is:", q.peek())
print("peeked value is:", q.peek())
# 구현된 클래스 import
from queue import Queue
q = Queue()
q.put(1)
q.put(5)
q.put(10)

print("my queue is :", q)
print("removved value is :", q.get())
print("my queue is:", q)
"""
print("peeked value is:", q.peek())  # 이렇게는 error
"""
print("peeked value is:", q.peek())  # 이렇게는 안되네 error
#일부러 넣은듯함, 검색해야 나오는 deque
print("my queue is:", q)
# list를 큐로 활용
q =[]
q.append(1)
q.append(5)
q.append(10)
print("my queue is:", q)
print("removved value is :", q.pop(0))
print("removved value is :", q.pop(0))
print("peeked value is:", q[0])
print("peeked value is:", q[0])
#큐의 활용
#프린터 인쇄 대기열##








