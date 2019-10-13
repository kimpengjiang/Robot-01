爬取福利网站，获取迅雷链接   
   
01版本：当前目录下生成“HaHaHa.txt”文档   
   
02版本：将生成文档修改为“index.html”文档，试图将其运行在服务器，但由于脚本中调用到pyqt5，无法在无头服务器上运行，暂时停止开发   
   
03版本：弃用pyqt5，改用Chrome headless（phantomjs现在也被selenium抛弃了，so~），目前的问题就是我在阿里云学生机上跑，负载能跑到14多……   
   
04版本：改成只取第一个迅雷链接，方便导入迅雷，同时发现chrome在调用后并不是直接关闭，而是会等待了一段时间，在windows上运行时出现多个chrome窗口，猜测这应该就是负载高的原因   

05版本：我是傻逼，在前面的版本中我一直都没有写close，导致打开的浏览器一直没有关闭，这才使得负载飙得贼高
   
环境：python3.7
   
   
服务器环境：   
centos7 + anaconda + chrome   
   
服务器环境搭建：   
anaconda安装：   
yum install bzip2   
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh # 可以去清华源下载最新版本
chmod +x Anaconda3-5.3.1-Linux-x86_64.sh   
./Anaconda3-5.3.1-Linux-x86_64.sh   
reboot # 重启或者重新加载下环境变量   
   
chrome安装：   
curl https://intoli.com/install-google-chrome.sh | bash # 这里为了方便，直接使用脚本安装   
google-chrome --version # 查看chrome版本   
wget https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip # 下载对应版本的chromedriver   
mv chromedriver /usr/bin/ # 把它丢到环境变量底下   
