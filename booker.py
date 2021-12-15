import requests
from bs4 import BeautifulSoup
from playsound import playsound
import time

pushpa_url = 'https://in.bookmyshow.com/guntur/movies/pushpa-the-rise-part-01/ET00129538'
far_from_url = 'https://in.bookmyshow.com/guntur/movies/spider-man-no-way-home/ET00310790'
request  = requests.get(pushpa_url)
htmlContent = request.text
with open('bms.html','w+',encoding='utf-8') as f:
    f.write(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')

book_tickets_btn = soup.find('button', {'data-phase':"postRelease"})
print(book_tickets_btn)

while True:
    print('checking')
    print(book_tickets_btn)
    if book_tickets_btn:
        playsound('BabyElephantWalk60.wav')
        print('playing sound using  playsound')
    time.sleep(180)
    