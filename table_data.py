url = "https://www.cisco.com/c/en/us/support/switches/catalyst-3750x-12s-e-switch/model.html?dtid=osscdc000283"

import requests
from bs4 import BeautifulSoup
import json

def find_eos_url(url):
    start_url = url
    download_html = requests.get(start_url)

    soup = BeautifulSoup(download_html.text, features="lxml")

    links = soup.find_all('a')

    #print(links[0].string)
    # print(len(links))
    for link in links:
        text = link.string
        # print(text)
        try:
            if text.startswith("End-of-Sale"):
                #print("znalezione end of sale")
                #print(link.get('href'))
                final_url = "https://www.cisco.com/" + link.get('href')
                return(final_url)
                break
        except:
            continue

url_to_eos = find_eos_url(url)
print(url_to_eos)

def get_table(url):
    start_url = url
    download_html = requests.get(start_url)

    soup = BeautifulSoup(download_html.text, features="lxml")
    # znajdz wszystkie kontenery z ogloszeniami
    try:
        full_table = soup.select('tbody')[0]
        return full_table
    except:
        print("nie znaleziono tabeli")

table = get_table(url_to_eos)

#print(table)

def read_table(table):
    data = {}

    soup = BeautifulSoup(str(table), 'html.parser')

    table_rows = soup.findAll("tr")
    counter = 0
    for row in table_rows:
        row_columns = row.findAll("td")
        #print(row_columns[0].p.string)
        #print(row_columns[2].p.string)
        print(counter)
        if counter == 1:
            data["End-of-Life Announcement Date"]=row_columns[2].p.string
        if counter == 2:
            data["End-of-Sale Date"]=row_columns[2].p.string
        if counter == 3:
            data["Last Ship Date"]=row_columns[2].p.string
        if counter == 4:
            data["End of SW"]=row_columns[2].p.string
        if counter == 5:
            data["End of Routine"]= row_columns[2].p.string
        if counter == 6:
            data["End of New Service"]= row_columns[2].p.string
        if counter == 7:
            data["End of Service Contract"]= row_columns[2].p.string
        if counter == 8:
            data["Last Date of Support"]= row_columns[2].p.string
        #print("read")
        counter+=1
    print(data)
    return data

read_table(table)
print("finished")
