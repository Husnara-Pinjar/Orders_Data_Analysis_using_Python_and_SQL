#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
#!pip install kaggle
import kaggle


# In[2]:


!kaggle datasets download ankitbansal06/retail-orders -f orders.csv


# In[3]:


#extract file from zip file
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


# In[4]:


#read data from file and handle null values
import pandas as pd


# In[5]:


df = pd.read_csv('orders.csv')
df.head(20)


# In[10]:


df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[14]:


#rename columns names ..make them lower case and replace space with underscore
#df.rename(columns={'Order Id':'order_id', 'City':'city'})
#df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)


# In[17]:


#derive new columns discount , sale price and profit
#df['discount']=df['list_price']*df['discount_percent']*.01
#df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df


# In[18]:


#convert order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[19]:


df.dtypes


# In[20]:


#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[21]:


df


# In[22]:


#load the data into sql server using replace option
import sqlalchemy as sal
engine = sal.create_engine('mssql://TOUQEER\SQLEXPRESS/master?driver=SQL+SERVER')
conn=engine.connect()


# In[24]:


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


# In[ ]:




