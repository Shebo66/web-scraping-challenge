from splinter import Browser
from bs4 import BeautifulSoup as soup
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path={'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()
    #set the url
    url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    #it will 2 seconds before it gets it from the page. It waits for page to fully load
    time.sleep(2)
    #get html off the page. html is used when we need to get someting from the page
    html=browser.html
    nasa_soup=soup(html,'html.parser')
    title=nasa_soup.find_all('div',class_='content_title')
    #print(title[1])
    news_title=title[1].get_text()
    print(news_title)

    paragraph=nasa_soup.find_all('div',class_='article_teaser_body')
    #print(paragraph[0])
    news_p=paragraph[0].get_text()
    print(news_p)

    url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    browser.links.find_by_partial_text('FULL IMAGE')[0].click()
    time.sleep(1)
    browser.links.find_by_partial_text('more info')[0].click()
    time.sleep(1)
    html=browser.html
    nasa_soup=soup(html,'html.parser')
    image=nasa_soup.find_all('figure',class_='lede')
    #print(image[0])
    image=image[0].find_all('a', href=True)[0]
    featured_image_url='https://www.jpl.nasa.gov/spaceimages'+image['href']
    print(featured_image_url)

    df=pd.read_html('https://space-facts.com/mars/')
    print(df[0])
    facts = df[0].to_html()

    #create a list (all four omages in a list)
    hemisphere_image_urls=[]
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    browser.links.find_by_partial_text('Hemisphere Enhanced')[0].click()
    time.sleep(1)
    html=browser.html
    nasa_soup=soup(html,'html.parser')
    image=nasa_soup.find_all('div',class_='downloads')
    #print(image[0])
    image=image[0].find_all('a', href=True)[0]
    hemisphere={}
    img_url=image['href']
    hemisphere['img_url']=img_url
    title=nasa_soup.find_all('h2',class_='title')
    hemisphere['title']=title[0].get_text()
    hemisphere_image_urls.append(hemisphere)
    browser.back()

    browser.links.find_by_partial_text('Hemisphere Enhanced')[1].click()
    time.sleep(1)
    html=browser.html
    nasa_soup=soup(html,'html.parser')
    image=nasa_soup.find_all('div',class_='downloads')
    #print(image[0])
    image=image[0].find_all('a', href=True)[0]
    hemisphere={}
    img_url=image['href']
    hemisphere['img_url']=img_url
    title=nasa_soup.find_all('h2',class_='title')
    hemisphere['title']=title[0].get_text()
    hemisphere_image_urls.append(hemisphere)
    browser.back()

    browser.links.find_by_partial_text('Hemisphere Enhanced')[2].click()
    time.sleep(1)
    html=browser.html
    nasa_soup=soup(html,'html.parser')
    image=nasa_soup.find_all('div',class_='downloads')
    #print(image[0])
    image=image[0].find_all('a', href=True)[0]
    hemisphere={}
    img_url=image['href']
    hemisphere['img_url']=img_url
    title=nasa_soup.find_all('h2',class_='title')
    hemisphere['title']=title[0].get_text()
    hemisphere_image_urls.append(hemisphere)
    browser.back()

    browser.links.find_by_partial_text('Hemisphere Enhanced')[3].click()
    time.sleep(1)
    html=browser.html
    nasa_soup=soup(html,'html.parser')
    image=nasa_soup.find_all('div',class_='downloads')
    #print(image[0])
    image=image[0].find_all('a', href=True)[0]
    hemisphere={}
    img_url=image['href']
    hemisphere['img_url']=img_url
    title=nasa_soup.find_all('h2',class_='title')
    hemisphere['title']=title[0].get_text()
    hemisphere_image_urls.append(hemisphere)
    browser.back()
    print(hemisphere_image_urls)



    # Store data in a dictionary
    mars_data = {
        "title": news_title,
        "paragraph": news_p,
        "mars_image": featured_image_url,
        "facts": facts,
        'hemispheres': hemisphere_image_urls
        
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
