import requests
import re
from bs4 import BeautifulSoup


def main():
    # откріваем сохраненную страничку
    html = open('req.html').read()

    #
    soup = BeautifulSoup(html,'lxml')

    #find возвращает объект первое найденое с условием
    #div = soup.find('div', class_='links')
    # OR
    div = soup.find('div', {'class': 'links'})
    print('1=========')
    print(div)
    #
    link = div.find_all('a')
    print('2=========')
    print(link)

    # FIND ALL
    print('3=========')
    link = soup.find_all('a')
    for a in link:
        print('------')
        ref = a.get('href')
        print(ref)
        print(a)


    print('4=========')
    # Поиск вверх к родителю
    # parent = find_parent() - find
    # parents = find_parents() - find_all
    h = soup.find('h1').find_parent('div', class_='two')
    # print(h)

    print('------')
    h = soup.find('h1').find_parent('div', class_='one')
    # print(h)

    print('------')
    h = soup.find('h1').find_parents('div')
    print(h)

    # test5 v5
    print('5=========')
    text = soup.find('h1').next_element
    print(text)

    # test6 v
    print('6=========')
    text = soup.find('h1').next_sibling
    print(text) #  пусто
    text = soup.find('h1').next_sibling.next_sibling
    print(text)  #<br/>
    text = soup.find('h1').next_sibling.next_sibling.next_sibling
    print(text)  #

    print('7=========')
    text = soup.find('h1').previous_sibling
    print(text)  #

    print('8=========')
    div = soup.find('h1').parent
    n = div.get('class')
    print(n)


    print('9= используем регулярные выражение ========')
    a = soup.find('a', href=re.compile('bing.com'))
    b = soup.find('a', href=re.compile('bing.com$'))
    c = soup.find('a', text=re.compile('second'))
    url1 = a.get('href')
    url2 = b.get('href')
    print("Выведет первую найденую",a)
    print(url1)
    print("Выведет вторую, у котоорой нет дополнительного пути",b)
    print(url2)
    print("Вывести первую найденую ссылку с текстом second",c)

    print('10= используем регулярные выражение ========')
    #12.04.2022
    regexp = r'\d{2}.\d{2}.\d{4}'
    a = soup.find('div', text=re.compile(regexp))
    print("Вернет div с датой ",a)
    print(a)

    a = soup.find('div', text=re.compile('sss'))
    print("Вернет div с текстом sss ", a)
    print(a)

    # пример
    regexp = r'\w\-'   # буквы, цифры, _ ,знак -
    regexp = r'/\d{1}$' # ищем строку с слешем и одной цифрой после которой ничего нет

    regexp = r'^post'  # будет искать блок у которого с начала строки текст с словом post
    a = soup.find('a', href=re.compile(regexp))
    print("----- ", a)
    print(a)

    regexp = r'post'  #  текст с словом post
    a = soup.find('a', href=re.compile(regexp))
    print("----- ", a)
    print(a)

if __name__ == '__main__':
    main()