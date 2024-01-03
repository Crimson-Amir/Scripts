from bs4 import BeautifulSoup
import requests


class Scrap:
    def __init__(self, link):
        self.link = link

    def get_currency(self):
        self.site = requests.get(self.link)
        self.soup = BeautifulSoup(self.site.content, 'html.parser')
        self.result = self.soup.find_all('tr')
        self.name = [{"name": curreency_name.th.text, "price": curreency_name.td.text} for curreency_name in self.result if curreency_name.get("class") == ["pointer"]]
        return self.name

# a = Scrap('https://www.tgju.org/currency')
# a.get_currency()
