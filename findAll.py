#findAll函数的使用
#find用法
#.fndAll("span",{"class":{"green","red"}})
#.fndAll({"h1","h2","h4"})



from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

namelst = bsObj.findAll("span", {"class":"green"})
for name in namelst:
    print(name.get_text())
