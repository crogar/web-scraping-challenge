import sys
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Mars News site
url = "https://redplanetscience.com/"

# instantiating the webdriver for Chrome!!!
browser.visit(url)
# Getting the webpage content
html = browser.html
# parsing our html plain text to a BS object
soup = BeautifulSoup(html, 'html.parser')
# Closing the driver(chrome instance)
browser.quit()
print(soup.prettify())

# Retrieve the parent divs for all articles
results = soup.find_all('div', class_='list_text')[0]  # using index 0 to get only the lastest news Title
# Storing the news title
news_title = results.find('div',class_='content_title').text
news_p = results.find('div',class_='article_teaser_body').text

print(f"Title: {news_title}")
print(f"Paragraph: {news_p}")

# instantiating our browser object
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://spaceimages-mars.com/'
# open browser and go to https://spaceimages-mars.com/
browser.visit(url)


# In[8]:


# obtaining featured image, knowing beforehand that the featured image tag has a class named "headerimage fade-in"
featured_image_url = browser.find_by_css('img[class="headerimage fade-in"]')['src'] # getting the src Attribute(image url path)


# In[9]:


featured_image_url


# <h2 style="color:green;text-align:center;"> Mars Facts </h2>

# In[10]:


url = 'https://galaxyfacts-mars.com/'


# In[11]:


# Use Panda's `read_html` to parse the url
tables = pd.read_html(url)


# In[12]:


len(tables)


# In[13]:


# Finding the table to use in our flask app
tables[0]


# In[14]:


df = tables[0]


# ##### Cleaning up table

# In[15]:


df.columns = ['Description','Mars','Earth']
df.head()


# In[16]:


# Resetting index
df.set_index(df.Description,inplace=True)
df


# In[17]:


html_table = df.to_html()


# In[18]:


print(html_table)


# <h2 style="color:green;text-align:center;">Mars Hemispheres </h2>

# In[19]:


#list that will be used to store titles and links to high resolution images
hemisphere_image_urls = []


# In[20]:


# instantiating our browser object
# browser = Browser('chrome', **executable_path, headless=False)
url = 'https://marshemispheres.com/'
# open browser and go to https://marshemispheres.com/
browser.visit(url)


# In[21]:


# creating a splinter.element_list.ElementList
hemispheres = browser.links.find_by_partial_text('Enhanced')


# In[22]:


for i in range(0, len(hemispheres)):
    try:
        browser.links.find_by_partial_text('Enhanced')[i].click()
        title = browser.find_by_css('h2[class="title"]').text
        img_url = browser.links.find_by_partial_text('Original')['href']
        hemisphere_image_urls.append({"title": title, "img_url": img_url})
        browser.visit(url)
    except Exception as e:
        print(e)


# In[23]:


print(hemisphere_image_urls)


# In[24]:


browser.quit()

