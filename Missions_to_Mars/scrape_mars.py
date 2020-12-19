# Import Dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd
from config import executable_path
from splinter import Browser

def init_browser():
    return Browser("chrome", executable_path, headless=False)

def scrape():
    browser = init_browser()

    ## Nasa Mars News ##

    # URL of page to be scraped
    url="https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #Retrieve latest news article and paragraph
    mars_news_title = soup.find_all('div', class_="content_title")[1].text
    mars_news_p = soup.find_all('div', class_="article_teaser_body")[0].text

    ## JPL Mars Space Images - Featured Image ##
   
    # URL to be scraped for mars image
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    html = browser.html
    soup_jpl = BeautifulSoup(html, "html.parser")
    # Search for featured image url link
    image_url= soup_jpl.find_all('article', class_="carousel_item")[0]['style'].split("('", 1)[1].split("')")[0]
    base_url = "https://jpl.nasa.gov"
    featured_image_url = base_url + image_url

    ## Mars Facts ##

    # Use pandas to get the tables in the webpage
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)
    tables = pd.read_html(mars_facts_url)
    MarsFacts = tables[0]
    MarsFacts.columns= ["Category", "Value"]
    MarsFacts=MarsFacts.set_index('Category')
    MarsFacts_html = MarsFacts.to_html()

    ## Mars Hemispheres ##

    # URL to be scraped for mars hemisphere images
    hemi_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)
    html=browser.html
    hemi_soup = BeautifulSoup(html, "html.parser")
    # Loop through all the links on the page to obtain images of each available hemispheres
    hemispheres = hemi_soup.find_all('div', class_ = 'description')
    hemisphere_images = []
    for i in range(len(hemispheres)):
    
        # Collect Title
        Title = hemispheres[i].h3.text
        print(Title)
        
        # Collect link
        SearchLink = hemispheres[i].a['href']
        
        # Get high res image
        high_res_search = "https://astrogeology.usgs.gov" + SearchLink
    
        browser.visit(high_res_search)
        html=browser.html
        high_res_soup = BeautifulSoup(html, 'html.parser')
        High_res = high_res_soup.find('div', class_="downloads").find('li').a['href']
        print(High_res)
        
        # Create Dictionary
        image_dict={}
        image_dict['title']=Title
        image_dict['img_url']=High_res
        
        hemisphere_images.append(image_dict)

        ## Mars Dictionary ##

        mars_dict = {}
        mars_dict = {"news_title":mars_news_title,
            "news_paragraph":mars_news_p,
            "featured_image_url":featured_image_url,
            "fact_table": str(MarsFacts_html),
            "hemisphere_images":hemisphere_images
        }
    return mars_dict