import requests, cloudscraper, cfscrape, selenium
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from datetime import time
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
    r = requests.get(url, headers=useragent, timeout = 60, proxies=proxy)
    result = r.text

    # спробуємо відкрити через wedriver якщо ресурс захищено cloudflare
    if r.status_code != 200 :
        # запуск браузера
        driver = webdriver.Firefox()
        driver.get(url)
        result = driver.page_source
        # зачиняємо сторінку та браузер
        driver.close()
        driver.quit()

    # зберігаємо отрману сторінку в файл
    with open('parsing.html','w') as file:
        file.write(result)

    return result

# Читаємо файл в список
def read_line(filename):
    line_lst = []
    with open(filename) as file:
        line_lst = file.read().splitlines()

    # return list words
    return line_lst

# ділимо речення на слова
def word_spliter(str):
    result = []
    ignore_symbol = ['-', '"', ',', '.', ';', '?', '!', '—']
    s2 = 'Th!i?s is, werwe                   my! s"tr,ing.'
    str_clean = str.translate({ord(x): '' for x in ignore_symbol})
    str_clean = str_clean.lower()
    result = str_clean.split()
    return result

# формуємо список слів отриманих з файлу
def all_words(filename):
    words = []
    with open(filename) as file:
        line = file.readline()
        while line:
            if line != '':
                list1 = word_spliter(line)
                for i in range(len(list1)):
                    words.append(list1[i])
                line = file.readline()

    # return list words
    return words

def main():
    #url = 'https://news.ycombinator.com/newest'
    #url = 'https://www.ukr.net'
    url = 'https://www.ukr.net/news/russianaggression.html'
    #url = 'https://translate.google.com.ua/?hl=uk#en/uk/python'

    # 1 відкрити сторінку з новинами (будь яку)
    #text_page = get_html(url)

    # 2 читаємо весь текст в список
    lst = read_line('parsing.html')
    print("Кількість строк в файлі",len(lst)+1)
    print("===============================================================")

    # формуємо файл тексту з сторінки
    page = BeautifulSoup(open('parsing.html').read(), 'lxml')
    print(page.text)
    print("===============================================================")

    # зберігаємо отрманий техт в файл та формуємо список слів з текста
    with open('parsing.txt', 'w') as file:
        file.write(page.text)
    list_words = all_words('parsing.txt')
    print(list_words)
    print("===============================================================")

    # 3 підрахувати частоту появи слів в тексті
    print("= 1 ==============================================================")
    print(f"== Загальна кількість слів в тексті === {len(list_words)} слів")
    print("= 2 Частота появи слів ===========================================")
    print(dict((x, list_words.count(x)) for x in set(list_words)))

    # 4 підрахувати кількість html-тегів
    # 5 підрахувати кількість посиланнь
    # 6 підрахувати кількість зображень


if __name__ == '__main__':
    main()
