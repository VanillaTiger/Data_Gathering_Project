from bs4 import BeautifulSoup

soup = BeautifulSoup('table.html.text', 'html.parser')

print(soup)