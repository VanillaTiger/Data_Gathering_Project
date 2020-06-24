import requests
from bs4 import BeautifulSoup
import json

devices_url = []
all_devices = []
all_eos_urls_product = []
eos_urls_product_url = []

all_data = []

#sciagnij strone z ofertami
start_url = "https://www.cisco.com/c/en/us/products/hw/tsd_products_support_end-of-sale_and_end-of-life_products_list.html"
download_html = requests.get(start_url)

soup = BeautifulSoup(download_html.text, features="lxml")
with open('downloaded.html', 'w', encoding="utf-8") as file:
    file.write(soup.prettify())

#znajdz wszystkie kontenery z ogloszeniami
mydivs = soup.findAll("div", {"class": "eol-listing-cq section"})

tiers = mydivs[0].findAll("div", {"class":"listing-3tier"})

for tier in tiers:
    content_links = tier.findAll("a", {"class": "contentLink"})
    for link in content_links:
        url = link.find('a', href=True)
        title = link.string
        url = link.get('href')
        url = "https://www.cisco.com" + url + "#~tab-documents"
        all_devices.append([title, url])
        devices_url.append(url)
    counter_sales=0
for device in devices_url:
    # sciagnij strone z ofertami
    start_url = device
    download_html = requests.get(start_url)

    soup = BeautifulSoup(download_html.text, features="lxml")

    # znajdz wszystkie kontenery z ogloszeniami
    mydivs = soup.findAll("ul", {"class": "doc-sublist"})
    for div in mydivs:
        try:
            if (div.h4 != None) & (div.h4.string == "End-of-Life and End-of-Sale Notices"):
                print("dodałem kolejną listę end of sales produktu " + str(counter_sales))
                # content_links_eos=div.findAll("a", {"class":"contentLink"})
                for link in div.find_all('a'):
                    url = link.get('href')
                    title = link.string
                    # print(title)
                    # print(link.get('href'))
                    url = "https://www.cisco.com" + link.get('href')
                    all_eos_urls_product.append([title, url])
                    eos_urls_product_url.append(url)
                counter_sales+=1
        except:
            continue

print("dlugos listy devices: ",len(devices_url))
print("dlugos listy products: ",len(eos_urls_product_url))

counter = 0
for product in eos_urls_product_url:
    # sciagnij strone z ofertami
    start_url = product
    download_html = requests.get(start_url)

    soup = BeautifulSoup(download_html.text, features="lxml")
    # znajdz wszystkie kontenery z ogloszeniami
    try:
        full_table = soup.select('tbody')[0]
        all_data.append(full_table)
    except:
        counter += 1
        continue
    print("dodałem kolejna tabele produktu " + str(counter))
    counter+=1

print("dlugos listy all data: ",len(all_data))
import csv

with open("all_eos_urls_product.csv", 'w', encoding='utf-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(all_eos_urls_product)