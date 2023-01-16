import requests, cloudscraper, cfscrape
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from random import choice


desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

def get_html(url, useragent=None, proxy=None):

    useragent = random_headers()
    print("html---------", useragent)
    #r = requests.get(url, headers=useragent, timeout=60)
    scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    r = scraper.get(url)

    # r = requests.get(url, headers=useragent, timeout = 60, proxies=proxy)
    print(r.status_code)
    return r.text

def get_0ip(html):
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip)
    print(ua)

def get_ip(html):
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('span', class_='ip').text.strip()
    ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()
    print(ip)
    print(ua)


def main():
    # ii and useragent
    url0 = 'https://sitespy.ru/my-ip'
    #url = 'https://www.ukr.net/'
    url = 'https://www.ukr.net/news/russianaggression.html'

    # набор user agent
    useragents = open('useragent').read().split('\n')
    #print(useragents[-1])

    # proxi
    proxies = open('proxy-list.txt').read().split('\n')
    #for i in proxies: print(i)
    #print(proxies[-1])

    #
    for i in range(1):
        proxy = {'http': 'http://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        print("11111111", useragent)
        print("22222222", proxy)
        try:
            html = get_html(url0, useragent)
            page = BeautifulSoup(html, 'html.parser')
            #print(page.text)
        except:
            continue

        #get_ip(html)

        #
        #scraper = cfscrape.create_scraper()
        #scraped_data = scraper.get('https://www.ukr.net/news/russianaggression.html')
        #print(scraped_data.text)

        #page = BeautifulSoup(scraped_data.text, 'html.parser')
        #print(page.text)
        #print(html)

        # ip install undetected-chromedriver
        driver = uc.Chrome()
        driver.get('https://www.ukr.net/news/russianaggression.html')



    #
    print('====================================================')
    #html = get_0(url0)
    #get_0ip(html)


if __name__ == '__main__':
    main()
