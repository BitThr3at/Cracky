from bs4 import BeautifulSoup
import re
import requests as req
import webbrowser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("keyword")
args = parser.parse_args()
keyword =args.keyword

resp = req.get("https://www.sadeempc.com/?s=" + keyword.replace(" ", "+"))
soup = BeautifulSoup(resp.content, "html.parser")
url_list = []
for link in soup.findAll('a', attrs={'href': re.compile(keyword.split(' ', 1)[0])}):
    url = link.get('href')

    if "#" not in url:
        url2 = url
        if "page" not in url2:
            url3 = url2
            if "category" not in url3:
                url_list.append(url3)

Furl_list = list(dict.fromkeys(url_list))
print(*Furl_list, sep = "\n")

for x in Furl_list:
    webbrowser.open(x, new=1, autoraise=True)


