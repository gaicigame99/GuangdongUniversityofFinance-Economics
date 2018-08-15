import urllib.request
from bs4 import BeautifulSoup
import ssl

# url = "http://news.baidu.com/"
# 机器人协议，可以看该网站对爬虫的限制
# "https://www.baidu.com/robots.txt"
url = "http://www.baidu.com/"

# 爬虫无法进就递交出入证
context = ssl._create_unverified_context()

response = urllib.request.urlopen(url, context=context)

# 打印的是二进制
# print(response.read())

# 打印HTML内容
html = response.read()
soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
# print(soup)

# 拿出所有a标签
links_a = soup.find_all('a')

for link in links_a:
    # 显示路径
    # print(link['href'])

    # 屏蔽内连接（拿到可用URL）
    # if "http://" in link['href'] or "https://" in link['href']:
    #     print(link['href'])

    # 拿到a标签括住的内容
    # link.get_text()

    if "http://" in link['href'] or "https://" in link['href']:
        print(link['href'], link.get_text())
