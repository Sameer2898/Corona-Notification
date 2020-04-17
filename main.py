from plyer import notification
from bs4 import BeautifulSoup
import time
import requests

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r'C:\Users\samee\OneDrive\Desktop\corona notifications\icon.ico',
        timeout = 15
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        myHtmlData = getData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        myDataStr = ''
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split('\n\n')
        states = ['Delhi', 'Haryana', 'Maharashtra', 'Punjab', 'Chandigarh']

        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states:
                nTitle = 'Case Of COVID-19'
                nText = f'State:- {dataList[1]}\nTotal Cases:- {dataList[2]}\nCured:- {dataList[3]}\nDeaths:- {dataList[4]}'
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)