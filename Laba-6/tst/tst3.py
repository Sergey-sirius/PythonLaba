from bs4 import BeautifulSoup
from selenium import webdriver

def main():
    #
    driver = webdriver.Chrome()
    driver.get('https://www.ukr.net/news/russianaggression.html')
    with open('index.html','w') as file:
        file.write(driver.page_source)

    #th2 = driver.find_element('h2')

    with open('index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src,"lxml")
    list1 = soup.find("article").text.strip()
    print("list", list1)
    #print(soup.text)


if __name__ == '__main__':
    main()