
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)


# In[4]:


acidentes = pd.read_csv("marijuana_e_acidentes.csv")
acidentes.dtypes


# In[7]:


frequencia = acidentes['Frequencia']
porcentagem = acidentes['Acidentes']
plt.pie(porcentagem, labels=frequencia, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Porcentagem de Acidentes por Frequencia de Uso de Marijuana')
plt.savefig('frequencia-pie.png')


# In[8]:


frequencia = acidentes['Frequencia']
porcentagem = acidentes['Motoristas']
plt.pie(porcentagem, labels=frequencia, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Porcentagem de Motoristas x Frequencia de Uso de Marijuana')
plt.savefig('motoristas-pie.png')

