import pandas as pd
from selenium import webdriver
import product_urls
import table_data

list_of_products = pd.read_excel("output.xlsx")

list_of_products= list_of_products.astype(str)

print(list_of_products.head())

print(list_of_products.at[0,'PRODUCT_ID'])

data = {}

for item in range(100,1000):
    id = list_of_products.at[item,'PRODUCT_ID']
    print("Przetwarzam item= ", item)
    #url_to_eos=table_data.find_eos_url(url)
    try:
        url = product_urls.get_product_url(id)
        table = table_data.get_table(url)
        data = table_data.read_table(table)
    except:
        list_of_products.at[item, "End-of-Life Announcement Date"]="no data"
        list_of_products.at[item, "End-of-Sale Date"] = "no data"
        list_of_products.at[item, "HW Last Ship Date:"] = "no data"
        list_of_products.at[item, "End of SW Maintenance Releases Date:"] = "no data"
        list_of_products.at[item, "End of Routine Failure Date:"] = "no data"
        list_of_products.at[item, "End of Service Contract Renewal Date:"] = "no data"
        list_of_products.at[item, "Last Date of Support:"] = "no data"
        continue
    try:
        list_of_products.at[item, "End-of-Life Announcement Date"]=data["End-of-Life Announcement Date"]
    except:
        list_of_products.at[item, "End-of-Life Announcement Date"]="no data"
    try:
        list_of_products.at[item, "End-of-Sale Date"]=data["End-of-Sale Date"]
    except:
        list_of_products.at[item, "End-of-Sale Date"]="no data"
    try:
        list_of_products.at[item, "HW Last Ship Date:"] = data["Last Ship Date"]
    except:
        list_of_products.at[item, "HW Last Ship Date:"] = "no data"
    try:
        list_of_products.at[item, "End of SW Maintenance Releases Date:"] = data["End of SW"]
    except:
        list_of_products.at[item, "End of SW Maintenance Releases Date:"] = "no data"
    try:
        list_of_products.at[item, "End of Routine Failure Date:"] = data["End of Routine"]
    except:
        list_of_products.at[item, "End of Routine Failure Date:"] = "no data"
    try:
        list_of_products.at[item, "End of Service Contract Renewal Date:"] = data["End of Service Contract"]
    except:
        list_of_products.at[item, "End of Service Contract Renewal Date:"] = "no data"
    try:
        list_of_products.at[item, "Last Date of Support:"] = data["Last Date of Support"]
    except:
        list_of_products.at[item, "Last Date of Support:"] = "no data"

    list_of_products.to_excel('output.xlsx')

