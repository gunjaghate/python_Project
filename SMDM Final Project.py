#!/usr/bin/env python
# coding: utf-8

# In[109]:


import numpy as np
import pandas as pd
from scipy.stats import f
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import scipy.stats as stats
from scipy.stats import ttest_1samp, ttest_ind
from statsmodels.stats.power import ttest_power


# In[56]:


df_wholesale = pd.read_csv("Wholesale Customer.csv")
df_wholesale.head(5)


# In[57]:


df_wholesale.shape


# In[58]:


df_wholesale.describe(include="all")


# From the above data it is clear that Top channel  purchasing items is Hotels. On an avarage most of the expendature has been done on Fresh Product(i.e : 12000.297727) 
# 

# In[59]:


df_wholesale["Channel"].value_counts(sort= False ).plot(kind="bar")


# From the bar graph we can say that Most of the HOTELS are spending omney on maintain their stock of different items in different different region.

# From above graph it is clear that Channel 'Hotel' have purchased Most and Channel 'Retail' have purchased least product from the wholesale distributor 

# In[60]:


df_wholesale["Region"].value_counts(sort= False ).plot(kind="bar")


# Items has got purchased by Other Region is much more greater than rest of the two region.

# In[61]:


df_grp_region = df_wholesale.groupby("Region").sum()
df_grp_region.describe()


# In[62]:


df_grp_Channel = df_wholesale.groupby("Channel").sum()
df_grp_Channel.describe()


# In[63]:


plt.figure(figsize=(7,10))
sns.boxplot(x="Region", y="Fresh",hue="Channel", data = df_wholesale)


# In[64]:


plt.figure(figsize=(7,10))
sns.boxplot(x="Region", y="Milk",hue="Channel", data = df_wholesale)


# In[65]:


plt.figure(figsize=(7,10))
sns.boxplot(x="Region", y="Grocery",hue="Channel", data = df_wholesale)


# In[66]:


plt.figure(figsize=(7,10))
sns.boxplot(x="Region", y="Frozen",hue="Channel", data = df_wholesale)


# In[67]:


plt.figure(figsize=(7,10))
sns.boxplot(x="Region", y="Detergents_Paper",hue="Channel", data = df_wholesale)


# In[68]:


plt.figure(figsize=(7,10))
sns.boxplot(x="Region", y="Delicatessen",hue="Channel", data = df_wholesale)


# In[69]:



from scipy.stats import variation 
variation(df_wholesale["Fresh"], axis = 0)


# In[70]:


variation(df_wholesale["Milk"], axis = 0)


# In[71]:


variation(df_wholesale["Grocery"], axis = 0)


# In[72]:


variation(df_wholesale["Frozen"], axis = 0)


# In[73]:


variation(df_wholesale["Detergents_Paper"], axis = 0)


# In[74]:


variation(df_wholesale["Delicatessen"], axis = 0)


# In[75]:


cor_Wholesale = df_wholesale.corr()


# In[76]:


sns.heatmap(cor_Wholesale,annot=True)


# In[77]:


# Grocery and Detegent_papers are highly related(0.92),Grocery and Milk are second highly related(0.73), Grocery and Milk are second highly related(0.73),Detergent_Paper and Milk are Third highly related(0.66)


# In[78]:


df_Survey = pd.read_csv("Survey-1.csv")


# In[79]:


df_Survey


# In[80]:


ct_Majors = pd.crosstab(df_Survey["Gender"],df_Survey["Major"])
ct_Majors["Total"] = ct_Majors.sum(axis = 1)
ct_Majors


# In[ ]:





# In[81]:


pd.crosstab(df_Survey["Gender"],df_Survey["Grad Intention"])


# In[82]:


pd.crosstab(df_Survey["Gender"],df_Survey["Employment"])


# In[83]:


pd.crosstab(df_Survey["Gender"],df_Survey["Computer"])


# # 2.2

# In[84]:


df_Survey["Gender"].value_counts()


# In[85]:


Pr_Male_outOf_all_Students = 29/62
Pr_Male_outOf_all_Students


# In[86]:


Pr_Female_outOf_all_Students= 33/62
Pr_Female_outOf_all_Students


# In[ ]:





# In[ ]:





# # 2.3

# In[87]:


Pr_Male_outOf_Major_Accounting = 4/29
print(Pr_Male_outOf_Major_Accounting)


# In[88]:


Pr_Male_outOf_Major_CIS = 1/29
print(Pr_Male_outOf_Major_CIS)


# In[89]:


Pr_Male_outOf_Major_EconomicsFinance = 4/29
print(Pr_Male_outOf_Major_EconomicsFinance)


# In[90]:


Pr_Male_outOf_Major_International_Business = 4/29
print(Pr_Male_outOf_Major_International_Business)


# In[91]:


Pr_Male_outOf_Major_Management = 6/29
print(Pr_Male_outOf_Major_Management)


# In[92]:


Pr_Male_outOf_Major_Other = 4/29
print(Pr_Male_outOf_Major_Other)


# In[93]:


Pr_Male_outOf_Major_Retailing_Marketing = 5/29
print(Pr_Male_outOf_Major_Retailing_Marketing)


# In[94]:


Pr_Male_outOf_Major_Undecided = 3/29
print(Pr_Male_outOf_Major_Undecided)


# In[95]:


Pr_Female_outOf_Major_Accounting = 3/29
print(Pr_Female_outOf_Major_Accounting)


# In[96]:


Pr_Female_outOf_Major_CIS = 3/29
print(Pr_Female_outOf_Major_CIS)


# In[97]:


Pr_Female_outOf_Major_EconomicsFinance = 7/29
print(Pr_Female_outOf_Major_EconomicsFinance)


# In[98]:


Pr_Female_outOf_Major_International_Business = 4/29
print(Pr_Female_outOf_Major_International_Business)


# In[99]:


Pr_Female_outOf_Major_Management = 4/29
print(Pr_Female_outOf_Major_Management)


# In[100]:


Pr_Female_outOf_Major_Other = 3/29
print(Pr_Female_outOf_Major_Other)


# In[101]:


Pr_Female_outOf_Major_Retailing_Marketing = 9/29
print(Pr_Female_outOf_Major_Retailing_Marketing)


# In[102]:


Pr_Female_outOf_Major_Undecided = 0/29
print(Pr_Female_outOf_Major_Undecided)


# # 2.4

# In[103]:


#2.4 a)
#no_of_male_inteded_to_grad=17
#total number of students = 62
Pr_Male_intend_Grad= 17/ 62
print(Pr_Male_intend_Grad)


# In[104]:


#2.4 b)
#no_of_female_dont have laptop = 4
#total number of students = 62
Pr_Female_intend_Grad= 4/ 62
print(Pr_Male_intend_Grad)


# # 2.5 

# In[105]:


#P(M or E) = P(M) +P(E)- P(M/E)
Prob_Male_or_Full_time_emp = (33/62) + (10/62)- (7/62)
Prob_Male_or_Full_time_emp


# In[106]:


# Probabilty of female student will be majoring in international business or management.
# prb_female_Stud_IB_or_Manage = Pr_Female_outOf_Major_International_Business * Pr_Female_outOf_Major_Management
prb_female_Stud_IB_or_Manage = 0.138  + 0.138
print(prb_female_Stud_IB_or_Manage)


# # 2.6

# In[111]:


pd.crosstab(df_Survey["Gender"],df_Survey["Grad Intention"]).drop("Undecided",axis =1)


# In[113]:


Prb_Female_outof_Intend_Grad  = 20/40
print("Prb_Female_outof_Intend_Grad ",Prb_Female_outof_Intend_Grad)
Prb_Yes_GradIntend = 18/ 40
print("Prb_Yes_GradIntend ",Prb_Yes_GradIntend)
Prb_female_Yes_intend_grad = 11/20
print("Prb_female_Yes_intend_grad ",Prb_female_Yes_intend_grad)


# # as p(f)+ p(y) < p(y/f)
# we can say that these two events are dependent

# In[115]:


#2.7


# # a)

# In[120]:


Total_GPA_Less_than_Three = df_Survey[df_Survey["GPA"] < 3].count()
Total_GPA_Less_than_Three


# In[ ]:


pro_Student_GPA_Less_than_Three = 17/62
print("pro_Student_GPA_Less_than_Three ",pro_Student_GPA_Less_than_Three )


# b)

# In[152]:


Prob_Male = 29/62
NumberOf_Male_Salary_Greater_than_50 = df_Survey[(df_Survey["Salary"] >= 50) & (df_Survey["Gender"] == "Male") ].count()


# In[153]:


NumberOf_Male_Salary_Greater_than_50


# In[154]:


Prob_M_Sal_gret_5 = 14/29
Prob_M_Sal_gret_5


# In[159]:


Prob_Female = 33/62
NumberOf_Female_Salary_Greater_than_50 = df_Survey[(df_Survey["Salary"] >= 50) & (df_Survey["Gender"] == "Female") ].count()


# In[160]:


NumberOf_Female_Salary_Greater_than_50


# In[165]:


Prob_Female_Sal_gret_5 = 18/33
print("Prob_Female_Sal_gret_5 ", Prob_Female_Sal_gret_5)


# # 2.8 

# In[183]:


figsize=(20,7)
sns.boxplot(y="GPA", data = df_Survey)


# In[185]:


figsize=(20,7)
sns.boxplot(y="Salary", data = df_Survey)


# In[187]:


figsize=(20,7)
sns.boxplot(y="Spending", data = df_Survey)


# In[189]:


figsize=(20,7)
sns.boxplot(y="Text Messages", data = df_Survey)


# In[192]:


df_asphalt = pd.read_csv("A & B shingles-1.csv")


# In[196]:


df_asphalt_A = df_asphalt["A"]
df_asphalt_A


# In[200]:


df_asphalt_B = df_asphalt["B"].dropna()
df_asphalt_B


# # step 1 H0: Mu = 0.35
#         ## H1: Mu > 0.35

# # step 2 alpha = 0.05

# # Step 3: Identify the test statistic
# We do not know the population standard deviation and n = 36. So we use the t distribution and the tSTAT test statistic.

# In[202]:


df_asphalt_A.describe()


# In[206]:


t_statistic, p_value = ttest_1samp(df_asphalt_A, 0.316667)
p_value/2


# In[208]:


df_asphalt_B.describe()


# In[210]:


t_statistic, p_value = ttest_1samp(df_asphalt_B, 0.273548)
p_value/2
# Accept Null Hypothesis


# # 3.2
# 

# In[212]:


t_statistic, p_value  = ttest_ind(df_asphalt_A,df_asphalt_B)
p_value

