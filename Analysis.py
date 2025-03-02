#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv('SPSS.csv')
print(data)


# In[2]:


data.describe()


# In[3]:


data.corr()


# In[4]:


panel_data = data.set_index(['Bank', 'Year'])
panel_data.describe()


# In[5]:


panel_data.corr()


# In[6]:


import statsmodels.api as sm
panel_data = data.set_index(['Bank', 'Year'])
y = panel_data['ROE']
X = panel_data[['CAR', 'GSIT', 'AAR', 'NPL']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


# In[7]:


from statsmodels.stats.outliers_influence import variance_inflation_factor
X = data.drop(columns=['ROE', 'Bank'])
X = sm.add_constant(X)
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)


# In[8]:


data.drop('NPL',axis=1,inplace=True)


# In[9]:


panel_data = data.set_index(['Bank', 'Year'])
panel_data.describe()


# In[10]:


panel_data.corr()


# In[11]:


import statsmodels.api as sm
panel_data = data.set_index(['Bank', 'Year'])
y = panel_data['ROE']
X = panel_data[['CAR', 'GSIT', 'AAR']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


# In[12]:


X = data.drop(columns=['ROE', 'Bank'])
X = sm.add_constant(X)
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_data)


# In[13]:


from linearmodels.panel import PanelOLS


# In[14]:


data.set_index(['Bank', 'Year'], inplace=True)
fe_model = PanelOLS.from_formula('ROE ~ CAR + AAR + GSIT + EntityEffects', data=data)
fe_results = fe_model.fit()
re_model = PanelOLS.from_formula('ROE ~ CAR + AAR + GSIT + RandomEffects', data=data)
re_results = re_model.fit()
print(fe_results)
print(re_results)


# In[15]:


import numpy as np
from scipy.stats import chi2


# In[16]:


fixed_effects_params = fe_results.params.values
fixed_effects_se = fe_results.std_errors.values
random_effects_params = re_results.params.values
random_effects_se = re_results.std_errors.values
diff_params = fixed_effects_params - random_effects_params
cov_matrix = np.outer(diff_params, diff_params) - np.outer(fixed_effects_se, fixed_effects_se)
hausman_statistic = diff_params @ np.linalg.inv(cov_matrix) @ diff_params
df = len(diff_params)
critical_value = chi2.ppf(0.95, df)
if hausman_statistic > critical_value:
    print("Hausman test rejects the null hypothesis. Use Fixed Effects.")
else:
    print("Hausman test does not reject the null hypothesis. Use Random Effects.")


# In[17]:


from linearmodels.panel import PanelOLS
re_model_robust = PanelOLS.from_formula('ROE ~ CAR + AAR + GSIT + EntityEffects', data=data)
re_results_robust = re_model_robust.fit(cov_type='robust')
print(re_results_robust)


# In[18]:


from statsmodels.stats.outliers_influence import variance_inflation_factor
X = data[['CAR', 'AAR', 'GSIT']]
vif = pd.DataFrame()
vif["Variable"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif)


# In[ ]:




