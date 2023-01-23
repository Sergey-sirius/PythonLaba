import requests
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

    # test5 v2
    print('5=========')


if __name__ == '__main__':
    main()