from bs4 import BeautifulSoup
import requests

def get_soup(text):
    """ Return BeautifulSoup object """  
    soup = BeautifulSoup(text, 'html.parser')
    return soup
def get_last_article(url, class_to_find):
    """ return the url of the last article published """
    html = requests.get(url)
    # get bs4.BeautifulSoup object
    soup_html = get_soup(html.text)
    # get bs4.element.Tag object
    link = soup_html.find(class_= class_to_find)
    return link.text, link.attrs['href']
