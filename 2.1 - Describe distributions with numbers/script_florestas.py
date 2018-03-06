
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)


# In[2]:


floresta = pd.read_csv("floresta.csv")
floresta.dtypes


# In[3]:


grupo1 = sns.barplot(x = 'Grupo 1', y = 'Grupo 1', data=floresta)
grupo1.set_ylim(0.0,35.0)
plt.savefig('grupo1-bar.png')


# In[4]:


grupo2 = sns.barplot(x = 'Grupo 2', y = 'Grupo 2', data=floresta)
grupo2.set_ylim(0.0,35.0)
plt.savefig('grupo2-bar.png')


# In[5]:


grupo3 = sns.barplot(x = 'Grupo 3', y = 'Grupo 3', data=floresta)
grupo3.set_ylim(0.0,35.0)
plt.savefig('grupo3-bar.png')


# In[6]:



sns.pointplot(x="Grupo 2", y="Grupo 2", color = 'red', data=floresta)
sns.pointplot(x="Grupo 3", y="Grupo 3", color = 'yellow', data=floresta)
pointp = sns.pointplot(x="Grupo 1", y="Grupo 1", color = 'green', data=floresta)
pointp.set(xlabel='', ylabel='Número de árvores')
#plt.show()
plt.savefig('comparação.png')

