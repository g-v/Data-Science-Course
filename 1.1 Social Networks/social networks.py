
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)


# In[2]:


networks = pd.read_csv("social_networks_data.csv")
networks.dtypes


# In[3]:


facebook = sns.barplot(x = 'Grupo de Idade', y = 'Usuarios de Facebook', data=networks)
facebook.set_ylim(0.0,25.0)
plt.savefig('facebook-bar.png')
# Podemos verificar que o grupo com maior % de usuarios do facebook eh o 25 a 34 anos, seguido do 35 a 44 e 45 a 54.


# In[4]:


twitter = sns.barplot(x = 'Grupo de Idade', y = 'Usuarios do Twitter', data=networks)
twitter.set_ylim(0.0,25.0)
plt.savefig('twitter-bar.png')
# # Podemos verificar que o grupo com maior % de usuarios do twitter eh o 25 a 34 anos, seguido do 18 a 24.


# In[5]:


linkedin = sns.barplot(x = 'Grupo de Idade', y = 'Usuarios do Linkedin', data=networks)
linkedin.set_ylim(0.0,25.0)
plt.savefig('linkedin-bar.png')
# Podemos verificar que os grupos com maior % de usuarios do linkedin sao 25 a 34 e 45 a 54 anos.


# In[6]:


idades = networks['Grupo de Idade']
facebook_users = networks['Usuarios de Facebook']
plt.pie(facebook_users, labels=idades, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Usuarios de Facebook por Grupo de Idade')
plt.savefig('facebook-pie.png')
# problemas com cores...


# In[7]:


twitter_users = networks['Usuarios do Twitter']
plt.pie(twitter_users, labels=idades, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Usuarios do Twitter por Grupo de Idade')
plt.savefig('twitter-pie.png')
# problemas com cores...


# In[8]:


linkedin_users = networks['Usuarios do Linkedin']
plt.pie(linkedin_users, labels=idades, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Usuarios do Linkedin por Grupo de Idade')
plt.savefig('linkedin-pie.png')
# problemas com cores...

