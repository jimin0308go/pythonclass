#!/usr/bin/env python
# coding: utf-8

# In[46]:


print("hello world")


# In[16]:


money = True
    
if money == True:
    print("use taxi")
else:
    print("walk")


# In[14]:


money = 2000

if money >= 5000:
    print("use taxi")
elif money >= 1000:
    print("use bus")
else:
    print("walk")


# In[29]:


grade = 50

if grade >= 90:
    print("grade A")
elif grade >= 80:
    print("grade B")
elif grade >= 70:
    print("grade C")
elif grade >= 60:
    print("grade D")
else:
    print("grade F")


# In[35]:


#while

no = 10

while no >= 0:
    print(no)
    no = no - 1


# In[39]:


promot = "1. 덧셈/ 2. 뺄셈 / 3, 곱셈/ 4, 너눗셈/ 5. 종료"
no = 0

while no <= 4:    
    print(promot)
    no = int(input())
    


# 

# In[ ]:


no = 0

while True:
    print(no)
    no = no + 1
    
    if no > 10:
        break


# In[ ]:


no = 0

while True:
    print(no)
    no = no + 1
    
    if no > 10:
        break


# In[49]:


no = 0

while True:
    print(no)
    no = no + 1
    
    if no > 10:
        break


# In[77]:


no = 1
sum = 0

while no <= 100:  
        no % 3 == 0
        sum = sum + no
        no = no + 3
        
    
        if no > 100:
            break
        
print(sum)


# In[79]:


no = 1
sum = 0

while no <= 100:
    if no % 3 == 0:
        sum = sum + no
        
    no = no +1
    
print(sum)


# In[80]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)


# In[85]:


math = [80,90,70,70,100]

j = 1
for i in math:
    if i >= 90:
        print(j, "pass")
    else:
        print(i, "fail")
    j += 1


# In[88]:


for i in [1,2,3,4,5,6,7,8,9,10]:
    if i%2==0:
        continue
        
        
    print(i)


# In[89]:


#range 함수

#숫자를 자동으로 생성해준다, for문과ㅓ 함께 사용되는 경우가 많다.

for i in range(1,11):
    print(i)


# In[109]:


#for 문으로 구구단 출력하기

for i in range(1,10):
    for j in range(2,10):
        print(j, "*", i, "=", j*i, end="\t")
    print()


# In[136]:


for i in range(1, 101,2):
    if i % 2 == 0:
        sum = sum + i
    
print(sum)


# In[130]:


# range를 사용하여 100이하의 수중 짝수들만의 합계

#range(start, stop, step)  start를 생략하면 0에서 시작, 
for i in range(0,11,3):
    print(i)
#stop을 생략하면 1씩 증가


# In[139]:


#리스트 축약/내포 list comprehension
#리스트를 좀더 편리하고 직관적올 만드는 방법이다.

list1 = [1,2,3,4]

print(list1)

list2 = [num             for num in list1]
print(list2)

list3 = [num*2            for num in list1]
print(list3)

list4 = [num            for num in list1 if num % 2 == 0]
print(list4)


# In[148]:


grade = 90

if grade >= 70:
    print("pass")
else:
    print("fail")
            

"pass"       if grade>80   else "fail"


# In[ ]:




