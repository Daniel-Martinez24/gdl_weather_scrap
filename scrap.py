from ast import main
import requests
from bs4 import BeautifulSoup

list_month = [
    '01-2022','02-2022','03-2022','04-2022','05-2022','06-2022',
    '01-2021','02-2021','03-2021','04-2021','05-2021','06-2021',
    '07-2021','08-2021','09-2021','10-2021','11-2021','12-2021',
]

def get_data(month)->None:

    URL = "https://www.tutiempo.net/clima/" +month+ "/ws-766120.html"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.findAll('table')

    # print(results[3].prettify())
    # print(results)
    #print(results[3].find_all("tr")[4])
    sta = results[3].findAll("tr")
    # print(sta[0].get_text())

    with open('./results/' +month +'.csv', 'w') as f:
        

            
        for _line in sta[:-2]:

            sta_th =_line.findAll("th")
            for _ in sta_th:
                # print(_.get_text(), end=' ')
                f.write(_.get_text() + ',')

            sta_td =_line.findAll("td")
            for _ in sta_td:
                # print(_.get_text(), end=' ')
                f.write(_.get_text() + ',')
            f.write('\n')



if __name__ == '__main__':
    for month in list_month:
        get_data(month)