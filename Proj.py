import requests
import webbrowser
from bs4 import BeautifulSoup
import urllib.request
import codecs
user = input("Enter something u want to search")
print("Searching..........")
google_search = requests.get("https://www.google.com/search?q=" + user)
soup = BeautifulSoup(google_search.text, 'html.parser')
search_results = soup.select('.r a')
for link in search_results[:7]:
    acatual_link = link.get('href')
    webbrowser.open('https://google.com/' + acatual_link)


def scrap(url):
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    print(soup.title)
    print((soup.title.string))
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    f = codecs.open("code.txt", "a+", "utf-8")
    for line in lines:
        print(line)
        line = line.replace("'", " ")
        f.write(line)
    f.close()
    D = {}
    for word in sorted(D.keys()):
        print(word, len(word))
    print(D)


scrap(input("paste the link for which u want to copy data"))
