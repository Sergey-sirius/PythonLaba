import requests
from bs4 import BeautifulSoup


#r = requests.get("https://news.ycombinator.com/newest")
r = requests.get("https://www.ukr.net")

#r = requests.get("https://translate.google.com.ua/?hl=uk#en/uk/python")

print(r.status_code)

if r.status_code == 200 :
    print(r.text[: 100])
    page = BeautifulSoup(r.text, 'html.parser')
    print("============================================")
    #print(page.text[: 2000])
    #print(page.text)
    #print(page.head.title.text)

    tbl_list = page.findAll('table')
    print(len(tbl_list))
    #print(tbl_list)
    print(page.table.text)