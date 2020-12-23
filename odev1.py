#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i=0
mylist=[]
while i<5:
    mylist.append(input("Enter a value:"))
    print("value:{}".format(mylist[i]))
    t= type(mylist[i])
    print(f'value type:{t}')
    i+=1

