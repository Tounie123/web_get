#!/bin/env python
import requests
import re
from bs4 import BeautifulSoup

heads = {}
heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

def get_last_page():
    response = requests.get("https://linux.cn/tech/desktop/",headers=heads)
    soup = BeautifulSoup(response.content, "html.parser")
    all_page = soup.find(class_="last")
    last_page = re.sub(r'\D',"",all_page.get('href'))

    return last_page

def get_one_page(num):
    url = "https://linux.cn/tech/desktop/index.php?page=" + str(num)
    response = requests.get(url,headers=heads)
    soup = BeautifulSoup(response.content, "html.parser")
    block = soup.find_all(attrs={'class':'block'})
    print(block)


def main():
    all_pages = get_last_page()
    #for i in range(1,int(all_pages)+1):
    #    get_one_page(i)
    get_one_page(43)


if __name__ == '__main__':
    main()
