import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    data_scraped = {}
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
  
    # Retrieve the parent divs for all articles
    results = soup.find_all('div', class_='list_text')[0]  # using index 0 to get only the lastest news Title
    # Storing the news title
    news_title = results.find('div',class_='content_title').text
    news_p = results.find('div',class_='article_teaser_body').text

    data_scraped["News_Title"] = news_title
    data_scraped["News_Paragraph"] = news_p
    
    # getting url for featured images
    url = 'https://spaceimages-mars.com/'
    # open browser and go to https://spaceimages-mars.com/

    browser.visit(url)

    # obtaining featured image, knowing beforehand that the featured image tag has a class named "headerimage fade-in"
    featured_image_url = browser.find_by_css('img[class="headerimage fade-in"]')['src'] # getting the src Attribute(image url path)
    data_scraped["Featured_img_url"] = featured_image_url
    
    # Obtaining Tables at the next link using pandas
    url = 'https://galaxyfacts-mars.com/'
    # Use Panda's `read_html` to parse the url
    tables = pd.read_html(url)

    # Finding the table to use in our flask app
    #tables[0]
    df = tables[0]

    # Cleaning up table
    df.columns = ['Description','Mars','Earth']

    # Resetting index
    df.set_index(df.Description,inplace=True)
    html_table = df.to_html()

    #Assigning the html table to key 'html_table'
    data_scraped['tableHtml'] = html_table.replace("border=\"1\" class=\"dataframe\"","class=\"table table-striped table-dark table-responsive\"")
    #list that will be used to store titles and links to high resolution images
    hemisphere_image_urls = []

    # Calling "visit" method to open browser and go the next url
    url = 'https://marshemispheres.com/'
    # open browser and go to https://marshemispheres.com/
    browser.visit(url)

    # creating a splinter.element_list.ElementList
    hemispheres = browser.links.find_by_partial_text('Enhanced')

    for i in range(0, len(hemispheres)):
        try:
            browser.links.find_by_partial_text('Enhanced')[i].click()
            title = browser.find_by_css('h2[class="title"]').text
            img_url = browser.links.find_by_partial_text('Sample')['href']
            hemisphere_image_urls.append({"title": title, "img_url": img_url})
            browser.back()
        except Exception as e:
            print(e)

    data_scraped['hemisphere_urls'] = hemisphere_image_urls
    browser.quit()
    return data_scraped