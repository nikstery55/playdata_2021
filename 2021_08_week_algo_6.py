#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
재귀함수 
메소드 혹은 함수의 내부에서 자기자신의 메소드 혹은 함수를 다시 호출하는 함수

"""


# In[1]:


#반복문을 활용한 완전탐색
data = [3, 5, 8]


# In[4]:


result = set()
for i in range(2):
    for j in range(2):
        for k in range(2):
            result.add(data[0] * i + data[1]*j + data[2]*k)

print(result)
"""
원하는 값 출력
"""


# In[ ]:


data = [ 3, 5, 7, 10, 12, 15, 20]
# 이 경우는 반복문을 사용할시 - 성분의 개수 = 반복문의 갯수 가된다 
#재귀함수로 이용하는것이 편하다


# In[ ]:


"""
재귀함수 사용 이유
- 코드의 간결화 및 변수 사용 최소화 
조건문을 활용하여 재귀함수 종료조건을 삽입
"""


# In[5]:


data = [3, 5, 8]

def recur(index, value):
    if index == len(data):
        result.add(value)  #재귀함수 종료 구문
    else:
        recur(index + 1, value + data[index])
        recur(index + 1, value)   # 재귀 함수 본문


# In[6]:


result = set()
recur(0, 0)
print(result)


# In[7]:


data = [3, 5, 8, 10, 12, 15, 20]
def recur(index, value):
    if index == len(data):
        result.add(value)  #재귀함수 종료 구문
    else:
        recur(index + 1, value + data[index])
        recur(index + 1, value)   # 재귀 함수 본문


# In[8]:



result = set()
recur(0, 0)
print(result)
# 재귀함수로 편리하게 결과 출력


# In[ ]:


"""
재귀 함수 활용
- 팩토리얼
"""


# In[9]:


def factorial(n):
    if n == 1:
        return 1
    
    else:
        return n * factorial(n-1)


# In[10]:


factorial(5)


# In[ ]:


"""
재귀함수 활용
- 피보나치 수열
"""


# In[11]:


def fibonacci(n):
    if n ==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# In[13]:


fibonacci(7)


# In[ ]:


"""
재귀함수 깊이
파이썬에서는 호출 1000번까지 허용되고 
그 이후는 오류를 출력함
하지만 재귀함수 깊이를 조정할수 있다
"""


# In[14]:


import sys
sys.setrecursionlimit(10**6)
"""
import sys
sys.setrecursionlimit(n)
이렇게 재귀함수 깊이를 조절할수 있다
"""


# In[ ]:




