# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# Lab 9
# Description:
# Describe what this program does in your own words such as:
'''
This program uses our newly learned concepts underlying webscraping to output website article titles and links.
'''
import os
import ssl
import urllib.request
from bs4 import BeautifulSoup as bs

def get_security_context():
    # Ignore certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def store_webpage(url, ctx, fn):
    page = urllib.request.urlopen(url, context=ctx)
    soup = bs(page.read(), 'html.parser')
    f = open(fn, 'w', encoding='utf-8')
    print(soup, file=f)
    f.close()

def load_webpage(url, ctx):
    page = urllib.request.urlopen(url, context=ctx)
    return bs(page.read(), 'html.parser')


def main():
    ctx = get_security_context()
    web_url = 'https://www.9to5mac.com/'
    file_name = 'mac_main.html'
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        store_webpage(web_url, ctx, file_name)
    file_url = 'file:///' + os.path.abspath(file_name)
    soup = load_webpage(file_url, ctx)
    # find all div tags with a class attribute of 'story-wrap'
    story_wraps = soup.find_all('a', class_='article__title-link')
    for story in story_wraps:
        # print(story)
        # grab the first h3 tag's content under this tag
        # print(story.h3)
        print(story.text)
        print(story['href'])

if __name__ == '__main__':
    main()