from bs4 import BeautifulSoup
import requests
url = "http://quotes.toscraps.com/"
try:
    response = requests.get(url)
    print(response.url,response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'lxml')
        quotes = soup.find_all('span',class_='text')
        authors = soup.find_all('small',class_='author')
        for i in range(len(quotes)):
            print(" {} by {} ".format(quotes[i].text,authors[i].text))
    else:
        print("error fetching content")
except:
    print("Error Getting Response")