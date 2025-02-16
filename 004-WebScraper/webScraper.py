


# weather website web scraping


import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    URL = "https://weather.com/en-IN/weather/today/l/f5720f935015d866abbc8f4d5beefe74b16a77fe84928669d117dd882d7de136"
    htmlPage = requests.get(URL)

    BeautifulSoup = BeautifulSoup(htmlPage.content, "html.parser")

    results = BeautifulSoup.find(id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034")
    currentTemp = results.find('span', class_="CurrentConditions--tempValue--zUBSz")
    descritpion = results.find('div', class_="CurrentConditions--phraseValue---VS-k")
    location = results.find('h1', class_="CurrentConditions--location--yub4l")
    timestamp = results.find('span', class_="CurrentConditions--timestamp--LqnOd")

    print(' -'*23)
    print("|","Current Temperature : ",currentTemp.text, "                |")
    print("|","Weather Description : ",descritpion.text, "               |")
    print("|","Location            :",location.text, "|")
    print("|","Local Time          :",timestamp.text, "     |")
    print(' -'*23)