import requests, cloudscraper, cfscrape
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from random import choice



html_tag =[
    '<!--...-->', '<a>', '<abbr>','<address>', '<applet>', '<area>', '<article>',
    '<aside>', '<audio>', '<b>', '<base>', '<basefont>', '<bdo>', '<big>',
    '<blockquote>', '<body>', '<br>', '<button>', '<canvas>', '<caption>', '<center>',
    '<cite>', '<code>', '<col>', '<colgroup>', '<datalist>', '<dd>', '<del>',
    '<details>', '<dfn>', '<dialog>', '<dir>', '<div>', '<dl>', '<!DOCTYPE>',
    '<dt>', '<em>', '<embed>', '<fieldset>', '<figcaption>', '<figure>', '<font>', '<footer>',
    '<form>', '<frame>', '<frameset>', '<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>',
    '<head>', '<header>', '<hgroup>', '<hr>', '<html>', '<i>', '<iframe>', '<img>',
    '<input>', '<ins>', '<kbd>', '<keygen>', '<label>', '<legend>', '<li>', '<link>',
    '<main>', '<map>', '<mark>', '<menu>', '<menuitem>', '<meta>', '<meter>', '<nav>',
    '<noscript>', '<object>', '<ol>', '<optgroup>', '<option>', '<output>', '<p>',
    '<param>', '<picture>', '<pre>', '<progress>', '<q>', '<rp>', '<rt>', '<ruby>',
    '<s>', '<samp>', '<script>', '<section>', '<select>', '<small>', '<source>',
    '<span>', '<strike>', '<strong>', '<style>', '<sub>', '<summary>', '<sup>', '<table>',
    '<tbody>', '<td>', '<textarea>', '<tfoot>', '<th>', '<thead>', '<time>', '<title>',
    '<tr>', '<track>', '<tt>', '<u>', '<ul>', '<var>', '<video>', '<wbr>'
]

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

# випадковий агент
def random_headers():
    return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

def get_html(url, useragent=None, proxy=None):
    # визначаємо який агент буде в запиті
    useragent = random_headers()

    #r = requests.get(url, headers=useragent, timeout=60)
    #scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    #r = scraper.get(url)

    r = requests.get(url, headers=useragent, timeout = 60, proxies=proxy)
    result = r.text

    # спробуємо відкрити через wedriver якщо ресурс захищено cloudflare
    if r.status_code != 200 :
        #print(r.status_code)
        driver = webdriver.Chrome()
        driver.get(url)
        result = driver.page_source

    with open('index.html','w') as file:
        file.write(result)

    return result

def main():
    #url = 'https://news.ycombinator.com/newest'
    #url = 'https://www.ukr.net'
    url = 'https://www.ukr.net/news/russianaggression.html'
    #url = 'https://translate.google.com.ua/?hl=uk#en/uk/python'

    # 1 відкрити сторінку з новинами (будь яку)
    text_page = get_html(url)
    print(text_page)

    # 2 читаємо весь текст в список
    # 3 підрахувати частоту появи слів в тексті
    # 4 підрахувати кількість html-тегів
    # 5 підрахувати кількість посиланнь
    # 6 підрахувати кількість зображень


if __name__ == '__main__':
    main()
