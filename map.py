#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import chart_studio.plotly as py
import plotly.offline as po
import plotly.graph_objs as pg
import requests


# In[2]:


po.init_notebook_mode( connected = True)


# In[3]:


url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "1293145f1amsh1fd6f0f82c5a680p1b6215jsn3dc6b068b7ed"
    }


# In[4]:


apidata = requests.request("GET", url, headers=headers).json()
countries = []
totalcases = []
deaths = []
text = []


# In[5]:


for i in range(213):
    countries.append(apidata['countries_stat'][i]['country_name'])
    totalcases.append(int(apidata['countries_stat'][i]['cases'].replace(',','')))
    deaths.append(int(apidata['countries_stat'][i]['deaths'].replace(',','')))
    text.append(f'{countries[i]}<br>Cases {totalcases[i]:,d}<br>Deaths {deaths[i]:,d}')


# In[6]:


apidict = {
    'countries':pd.Series(countries),
    'total cases':pd.Series(totalcases),
    'deaths':pd.Series(deaths),
    'text':pd.Series(text)
}


# In[7]:


df = pd.DataFrame(apidict)


# In[18]:


data = dict(type='choropleth',
            locations = list(df['countries']),
            locationmode = 'country names',
            z = list(df['total cases']),
            text = df['text'],
            hoverinfo='text',
            colorscale = 'viridis',
            colorbar = dict(title = 'Total Cases'),
            reversescale = True )


# In[19]:


layout = dict(title='Covid-19 Cases Around the World', geo = {'scope':'world'})


# In[20]:


x = pg.Figure(data=[data], layout=layout)


# In[21]:


po.plot(x, filename='index.html')







# In[ ]:




