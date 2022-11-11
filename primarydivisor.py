#!/usr/bin/env python
# coding: utf-8

# In[1]:


# number=int(input('enter a number'))

def least_prime_divisor(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return i
    return n

def prime_factor(n):
    answer={}
    while n!=1:
        temp=least_prime_divisor(n)
        if temp in answer:
            answer[temp]+=1
        else:
            answer[temp]=1
        n=int(n/temp)
    # print(answer)
    return answer

primefactorlist=[]
result={}
for i in (123,43,54,12,76,84,98,678,543,231):
    
    # primefactorlist.append(len(prime_factor(i)))
    
    result[i] =len(prime_factor(i))

print(result)
max_keys = [key for key, value in result.items() if value == max(result.values())]
print(f'the keys with the maximum value are {max(max_keys)}with {max(result.values())} factors')

    


# In[ ]:




