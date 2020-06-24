from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

id = 'WS-C3750X-12S-E-WS'

def get_product_url(id):
    product_id = id
    url="https://search.cisco.com/search?query=" +\
    product_id +\
    " end-of-sale" +\
    "&locale=enUS&bizcontext=&cat=&mode=text&clktyp=button&autosuggest=false"

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome("C:/Users/Adam/.wdm/drivers/chromedriver/83.0.4103.39/win32/chromedriver.exe", options=chrome_options)
    driver.get(url)
    time.sleep(2)

    item = driver.find_element_by_xpath("//*[@id='results']/div/div[1]/div/div/div[5]/div/div[1]/span/a")
    item.click()

    print("product url=" + driver.current_url)
    return driver.current_url

get_product_url(id)
