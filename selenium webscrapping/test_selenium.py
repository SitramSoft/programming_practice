from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

browser_options = Options()  
browser_options.add_argument("--headless")  

driver = webdriver.Chrome(options=browser_options)
driver.get('https://www.nasa.gov')
headlines = driver.find_elements_by_class_name("headline")
for headline in headlines:
    print(headline.text.strip())
driver.quit()