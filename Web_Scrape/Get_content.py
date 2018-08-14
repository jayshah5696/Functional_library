def gethtml(url):
  '''Geting Html page from the link'''
  import requests
  from bs4 import BeautifulSoup
  web = requests.get(url)
  content = BeautifulSoup(web.content,'html.parser')
  return content


# Getting only wiki internal Links
  def getLinks(articleUrl):
  '''Getting internal Article page links from the Article (internal page link) Url from the wiki Website'''
  bsObj = gethtml("http://en.wikipedia.org"+articleUrl)
  return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
