import requests
import lxml
from bs4 import BeautifulSoup


def scrape_wiki_homepage():
    
    URL = "https://en.wikipedia.org/wiki/Main_Page"
    
    response = requests.get(URL)
    
    with open('response.txt','w') as f:
        f.write(response.text)
        
        
    bs = BeautifulSoup(response.text, 'lxml')
    
    div = bs.find('div',id='mp-tfa')
    
    featured_article = div.find('p')
    
    featured_article_title = featured_article.find('b').find('a').getText()
    
    print(str(featured_article_title))
    
    


if __name__=="__main__":
    scrape_wiki_homepage()
        