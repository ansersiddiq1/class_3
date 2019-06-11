#!/usr/bin/env python
# coding: utf-8

# # list

# In[1]:


l1 = ["Anser",27,2,7.0,True]
l1


# In[3]:


dir(l1)


# In[6]:


type(l1)


# # list indexing

# In[7]:


l1


# In[9]:


a = "ANUS AHMED"
a= a[-1::-1]
a


# In[11]:


a = True
a


# In[12]:


l1


# In[13]:


l1[-1]


# In[14]:


l1[2]


# In[15]:


l1[0]


# In[17]:


l1[3]


# In[19]:


l1[-3]


# In[20]:


len(l1) # to find the length of list


# In[22]:


l1


# In[24]:


l1[1] = 89
l1


# In[21]:


l2 = [1,7,9,8,15,30]
l2


# In[25]:


l1[-2] = 1000
l1


# In[27]:


l1[-3] = 2000
l1


# In[28]:


l1[2] = "Anus" ; l1


# In[30]:


i = 0
while i < len(l1):
    print(l1[i])
    i=i+1


# In[37]:


i = 0
while i >=0 :
    print(l1[i])
    i = i - 1


# In[41]:


sorted(l2)


# In[45]:


l2.reverse() # this is also use to reverse
l2


# In[48]:


sorted(l2, reverse=True) # kisi function ko true kr skte hain is trha


# In[50]:


l2.pop()
l2


# In[51]:


l2.pop() # last wala chor k nbaki sub print kr waye ga
l2


# In[52]:


l2


# In[53]:


l2 = [30,15,9,8,7,1]
l2


# In[54]:


l2.sort() #to reverse 
l2


# # range(start,end,step)
# start = include
# end = exclude
# step = sequence

# In[55]:


range(1,11)


# In[56]:


range(11)


# In[59]:


list(range(1,11))


# In[65]:


for i in range(1,50):
    print(i)


# In[67]:


list(range(1,101,10))


# In[68]:


for i in range(0,10,2):
    print(i)


# In[70]:


for i in range(0,51,2):
    print(i)


# In[71]:


l2


# In[72]:


l1


# In[73]:


chr(65)


# In[74]:


chr(1)


# In[75]:


chr(90)


# In[76]:


ord('W')


# In[77]:


ord('e')


# In[78]:


chr(100)


# In[79]:


l1 = list(range(65,91))
l1


# In[82]:


for e in  l1:
    print(chr(e))


# In[85]:


for e in l1:
    print(l1)


# In[86]:


list(map(chr,l1))


# In[89]:


l1 = ['anser','anus','anus k abbu anser']
list(map(len,l1))


# In[91]:


chr(48)


# In[93]:


for i in range(48,58):
    print(i)


# In[117]:


l1 = list(range(48,58))
print(*l1,sep=" ")


# In[98]:


for i in l1:
    print(i)


# In[99]:


for i in l1:
    print(chr(i))


# # SLICING
# #obj[start(include):end(exclude):step(step)]

# In[106]:


l1 = list(range(1,11)) ; l1


# In[113]:


l1[0:5]


# In[120]:


l1 = list(map(chr,list(range(65,91)))) ; print(*l1,sep=",")


# In[118]:


print(*l1,sep="-")


# In[121]:


l1[0:10]


# In[123]:


l1[0:26]


# In[126]:


l1[-26::]


# In[128]:


l1[::]


# In[130]:


l1[::-1]


# In[134]:


l1[::25]


# In[135]:


l1


# In[139]:


l1[5::20]


# In[142]:


l1[-20::-1]


# In[144]:


a = "ANUS AHMED" ; a = a[-1::-1] ; a


#  

# In[146]:


l1[:2] + l1[-3:]


# In[147]:


for e in l1:
    print(l1)


# In[149]:


l1 = list(map(chr,list(range(65,91)))) ; l1


# In[150]:


a = 5
'pakistan' if a==5 else 'china'


# In[151]:


["{} X {} = {}".format(2,4,4*2)]


# In[152]:


a= 5
for i in range(1,11):
    print(a ,"x",i,"=",a*i)


# In[153]:


[x for x in range(1,11)]


# In[155]:


for e in range(1,1001):
    if e%5==0 and e%7==0 and e%40==0:
        print(e)


# In[164]:


a= 7
a


# In[ ]:




