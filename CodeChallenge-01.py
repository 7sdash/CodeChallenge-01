
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


df= pd.read_csv('C:/Users/sOumyaz D/Documents/DS-Learn/CodeChallenge/SoftwareEngineer-Summer-2018-master/input.txt')


# In[ ]:


df


# In[ ]:


df.describe()


# In[ ]:


Vec1 = df['Index']
print(Vec1)


# In[ ]:


tot = 1000000
Val = 0.0


for i in Vec1[9:]:
    if Val <= tot:
        Val += i
        
print(Val)    

