# Every body knows that links that contain meaning less characters gibrish are hard to remember! so, instead We're
# gonna use the format of the link as an Adjective+Noun, to make it easy to remember. Here is a script to scrape the
# internet to find adjectives and nouns..


import requests
from bs4 import BeautifulSoup
import os


def get_soup(url):
    return BeautifulSoup(requests.get(url).content, "lxml")


def get_data(data):
    if data == "adjs":
        url = "https://www.talkenglish.com/vocabulary/top-500-adjectives.aspx"
    elif data == 'nouns':
        url = "https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx"
    else:
        return

    soup = get_soup(url)
    soup = soup.findAll('table')
    soup = soup[1]
    A = soup.findAll('a')
    A = [a.text+'\n' for a in A]
    return A


def main():
    List = ['nouns', 'adjs']
    for data in List:
        data_list = get_data(data)
        with open(os.path.join(os.getcwd(), 'home', data+'.txt'), 'w') as f:
            f.writelines(data_list)


if __name__ == '__main__':
    main()
