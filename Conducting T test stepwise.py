#!/usr/bin/env python
# coding: utf-8

# ### First we import and install all required packages

# In[2]:


# Importing all required packages
import numpy as np
import pandas as pd
import os
import scipy.stats as stats


# ### Checking the current working directory

# In[3]:


# Checking the working directory of this project
os.getcwd()


# ### Chaning the current working directory to a specified directory

# In[4]:


# Changing the working directory for this project
os.chdir("F:\ANACONDA\PYTHON FILES")


# ### Finally checking the current working directory to move forward

# In[5]:


# Checking the new changed directory
os.getcwd()


# ## **Note** : The file scores.csv is saved in the same directory as the current working directory

# ### Reading the scores.csv file using read_csv() function of pandas library

# In[6]:


# Reading the scores.csv file in a variable named df 
df=pd.read_csv("scores.csv")


# ### Reading the file if it is in .xlsx format, we use read_excel() function of pandas library

# In[7]:


# Reading the same data using the data1.xlsx file
df1=pd.read_excel("data1.xlsx")


# ### Data Understanding steps: Basic commands- .head(),.columns ,.shape etc

# In[8]:


# Checking the first 10 rows of this data frame called df
df.head(10)


# #### Checking the first 10 rows of the excel file

# In[9]:


# Checking the first 10 observations of the df1 data set
df1.head(10)


# In[10]:


# Getting the column names of the dataframe df
df.columns.values


# In[11]:


# Getting the shape od the data frame called df
df.shape


# ### Basic Data Manipulation process: Converting the data into categorical data

# In[31]:


# Converting the Gender column in two categories namelt male and female
# df['gender']=df['gender'].astype('category')


# ## Checking for the Normality of data
# 
# #### To check data is normal or not we use the shapiro test. If the calculated P value is greater than 0.05, then we conclude that the data is normally distributed. Then only we can move to the next part. To conduct the normality test we consider the math score of females and males. We conduct shapiro test on both of them and then observe the P value.

# In[12]:


# Selecting the input variables fm_math and mm_math for females and males score respectively
fm_math=df.loc[df['gender']=='female','math score']
mm_math=df.loc[df['gender']=='male','math score']


# In[13]:


# Printing the output and sample size
print(fm_math)
fm_math.size


# In[14]:


# Printing the second output and the sample size
print(mm_math)
mm_math.size


# In[22]:


# Applyting shapiro test on the whole data
maths_score = df['math score']
maths_score
w,p = stats.shapiro(maths_score)
print('Test Statistics Value:',w)
print('P Value for this data:',p)
alpha=0.05
if p > 0.05:
    print('Accept Null Hypothesis- The data is Normally Distributed')
else:
    print('Reject Null Hypothesis- The data is not normally distributed')


# In[15]:


# Conducting the shapiro test for the fm_math 
w,p = stats.shapiro(fm_math)
print('Test statistics value for fm_math:',w)
print('P value for fm_math:',p)
# We observe that P value is less than 0.05
# Implies fm_math does not follow normality
p < 0.05


# In[16]:


# Conducting the shapiro test for the mm_math 
w,p = stats.shapiro(mm_math)
print('Test statistics value for fm_math:',w)
print('P value for fm_math:',p)
p < 0.05
# We observe that P value is greater than 0.05
# Implies fm_math  follow normality


# #### Here we observe that the sample sizes are large. So we use the Kolmogorov test to conclude on normality.

# In[17]:


# For fm_math data
ks_stat,p_value = stats.kstest(fm_math,'norm',args=(0,1))
print('Test statistics value for fm_math:',ks_stat)
print('P value for fm_math:',p_value)
p < 0.05


# In[18]:


# Since here the samples are large in size so we use Kolmogorov test to detect normality
# For mm_math data
ks_stat,p_value = stats.kstest(mm_math,'norm',args=(0,1))
print('Test statistics value for mm_math:',ks_stat)
print('P value for mm_math:',p_value)
p < 0.05


# #### Now as shapiro and kolmogorov test fails, we move to non parametric Mann-Whitney test

# In[19]:


# Performing Mann-Whitney test
stat, p_value = stats.mannwhitneyu(fm_math,mm_math)
print('Test statistics value:',stat)
print('Corresponding P value:',p_value)
alpha= 0.05
if p > alpha:
    print('CONCLUSION:Accept Null Hypothesis- Two Populations are Equal respect to Central Tendencies')
else:
    print('CONCLUSION:Reject Null Hypothesis- Two Populations are Not Equal respect to Central Tendencies')


# ### Now we can colclude what we observe by conducting these tests:
# * The data we have is not normally distributed.
# * To check normality we use Shapiro and Kolmogorov test which are parametric test.
# * After faliure we conduct Mann-Whitney U test
# * From that we conclude that the data we have is not same in terms of central tendencies.
