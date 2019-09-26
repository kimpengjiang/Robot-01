import requests
import re
import sys
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from datetime import datetime

def getURLList(url):
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
    response = requests.get(url,headers=header)
    list_a = re.findall('<a class="movie-box" href="(.*?)">',response.text)
    return list_a

class MyWebBrowser(QWebEnginePage):
    app = None
    def __init__(self):
        if MyWebBrowser.app is None:
            MyWebBrowser.app = QApplication(sys.argv)
        super().__init__()
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)

    def downloadHtml(self, url):
        self.load(QUrl(url))
        print("\nDownloadDynamicPage", url)
        MyWebBrowser.app.exec_()
        return self.html

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        MyWebBrowser.app.quit()

def useWebEngineMethod(url):
    """
        使用PyQt5的网页组件下载完整的动态网页
    """
    webBrowser = MyWebBrowser()
    html = webBrowser.downloadHtml(url)
    # print(html)
    data1 = re.findall('<a style="color:#333" rel="nofollow" title="滑鼠右鍵點擊並選擇【複製連結網址】" href="(.*?)">',html)
    # print(data1)
    for i in data1:
        with open("index.html", "a+", encoding="utf-8") as f:
            f.write("<p>"+i+"</p>"+"\n")
            f.close()


if __name__=='__main__':
    url = "https://www.dmmsee.icu/"
    dt = datetime.now()
    data = dt.strftime('%Y-%m-%d %H:%M:%S %p')
    with open("index.html",'w+',encoding='utf-8') as f:
        f.write("<h1><font color=red>更新于："+str(data)+"</font></h1>")
        f.close()
    for i in getURLList(url):
        with open("index.html","a+",encoding="utf-8") as f:
            f.write("\n")
            f.write("<h1>"+i+"</h1>"+"\n")
            f.close()
        useWebEngineMethod(i)