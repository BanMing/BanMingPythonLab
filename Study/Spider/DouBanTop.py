import requests
from bs4 import BeautifulSoup

doubanUrl = 'https://movie.douban.com/top250?start='


def GetMovies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    movieList = []
    for index in range(0, 10):
        req = requests.get(doubanUrl+str(index*25),
                           headers=headers, timeout=(10))
        # print(req.text)
        # print(str(index+1),'页面响应状态码：',req.status_code)
        soup = BeautifulSoup(req.text, 'lxml')
        divList = soup.find_all('div', class_='hd')

        # for each in divList:
        #     movie = each.a.span.text.strip()
        #     print(each.a.find_all('span')[0].text+each.a.find_all('span')[1].text)
        #     movieList.append(movie)
            # break
        bdList= soup.find_all('div',class_='bd')
        for item in bdList:
            print(item.p.text)
    return movieList


movies=GetMovies()
# print(movies)
