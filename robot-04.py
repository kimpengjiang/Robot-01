import requests
import re
from datetime import datetime
from selenium import webdriver

def getURLList(url):
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
    response = requests.get(url,headers=header)
    list_av_url = re.findall('<a class="movie-box" href="(.*?)">',response.text)
    list_len = len(list_av_url)
    return list_av_url,list_len

def getPageSource(url):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # client = webdriver.Chrome(chrome_options=chrome_options)
    client = webdriver.Chrome()
    client.get(url)
    html = client.page_source
    return html

def getXunLeiURL(url):
    html = getPageSource(url)
    data1 = re.findall('<a style="color:#333" rel="nofollow" title="滑鼠右鍵點擊並選擇【複製連結網址】" href="(.*?)">', html)
    # print(data1)
    i = data1[0]
    with open('list.txt', 'a+', encoding='utf-8') as f:
        f.write("\n")
        f.write(i)
        f.close()

if __name__=='__main__':
    url = "https://www.dmmsee.icu/"
    dt = datetime.now()
    data = dt.strftime('%Y-%m-%d %H:%M:%S %p')
    x,y = getURLList(url)
    with open('list.txt','w+',encoding='utf-8') as f:
        f.write(str(data)+"  "+str(y))
        f.close()
    for i in x:
        # with open('list.txt','a+',encoding='utf-8') as f:
        #     f.write("\n")
        #     f.write(i)
        #     f.close()
        getXunLeiURL(i)
