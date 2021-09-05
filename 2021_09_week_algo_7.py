#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
동적계획법

다이나믹 프로그래밍 라고도 불리며
하나의 큰 문제를 여러 개의 공통되는 작은 문제로 나누어서 
작은 문제의 정답들을 결합하여 알고리즘을 푸는 과정

- 규칙을 찾는 방법
"""


# In[ ]:


"""
점화식
- 수열에서 n번째 항을 이전에 나온 항들로 나타낸 공식
"""


# In[ ]:


"""
동적계획법 접근방법
- Bottom Up 방법 - 작은 문제에서 큰 문제로 반복문 호출
- Top Down 방법 - 큰 문제에서 작은 문제로 재귀 호출
"""


# In[4]:


"""
피보나치 수열 - Bottom up
"""
def fib(n):
    fibList=[1, 1]
    for i in range(2, n+1):
        fibList.append(fibList[i - 2]+ fibList[i-1])
    return fibList[-1]


# In[5]:


"""
피보나치 수열 - Top Down
이방식으로 하면 하나의 피보나치 수열을 구하기 위해서 많은 계산 중복이 발생됨 
- 해결 방법 - 메모이제이션
"""
def fib(n):
    if n ==0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# In[6]:


# 메모이제이션
"""
배열 혹은 해시를 활용하는것이 핵심
"""
memo = {0:1, 1:1}
def fib(n):
    if n in memo:
        return memo[n]
    else:
        result = fib(n-1) + fib(n-2)
        memo[n] = result
        return result


# In[7]:


#이웃하지 않는 숫자들의 합의 최댓값은?
data = [3, 4, 5, 6, 1, 2, 5]


# In[8]:


"""
동적계획법 예시
data = [ a0, a1, a2, a3, a4, a5, a6]
Sn = max(Sn-1, Sn-2 + an)
""" 
def solution(data):
    if len(data) == 1:
        return data[0]
    result = [data[0], max(data[0], data[1])]
    for i in range(2, len(data)):
        result.append(max (result[i-1], result[i-2] + data[i]) )
    
    return result[-1]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




