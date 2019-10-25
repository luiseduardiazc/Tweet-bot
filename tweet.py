from scraping.article import get_last_article
from config.conf import create_api

# for manage loop time
import time
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()

@tl.job(interval=timedelta(hours=12))
def make_tweet():
    """ this function create a tweet every 12 hours """
    api = create_api()
    url = 'https://news.ycombinator.com/'
    class_to_find = 'storylink'
    text, url = get_last_article(url,class_to_find)
    tweet = text + '\n' + url
    api.update_status(tweet)

if __name__ == "__main__":
    tl.start(block=True)