#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import colorsys
plt.style.use('seaborn-talk')
import os
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


pwd


# In[70]:


df = pd.read_csv(r"C:\Users\Natalia\Desktop\Trainee\MLS_Salaries.csv", sep= ',', low_memory=False)
df.head()


# In[89]:


print (df.head())


# In[76]:


print (df.describe('')) 


# In[3]:


plt.xlabel("Club")
plt.ylabel("Position")
plt.title("Total")
plt.show()


# In[33]:


variable.columns


# In[38]:


print(variable)


# In[47]:


print(df['Season;Club (grouped);Club;First Name;Last Name;Position;Total Compensation;Base Salary'])


# In[69]:


df.groupby(['Season;Club (grouped);Club;First Name;Last Name;Position;Total Compensation;Base Salary']).mean().sort_values('Season;Club (grouped);Club;First Name;Last Name;Position;Total Compensation;Base Salary')


# In[95]:


series_obj = Series(np.arrange(8), index=['row 1,'])


# In[ ]:




