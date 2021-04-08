# Check if USA is member of WHO website

# - go to https://www.who.int/
# - click on "Countries"
# - click on "All Countries"
# - Filter by region: type 'americas' and click on 'Region of Americas'
# - Assert if 'United States of America' is on the page

# Prerequisites:
#   Installing Selenium libraries - https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/
#   Installing WebDriver binaries - https://www.selenium.dev/documentation/en/selenium_installation/installing_webdriver_binaries/
#     Selenium requires a driver to interface with the chosen browser. 
#     Chrome:   https://sites.google.com/a/chromium.org/chromedriver/downloads
#     Edge:     https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
#     Firefox:  https://github.com/mozilla/geckodriver/releases
#     Safari:   https://webkit.org/blog/6900/webdriver-support-in-safari-10/

from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  
from selenium.common.exceptions import NoSuchElementException

# The url under test
url = "https://www.who.int/"

# Creating the browser object using the ChromeDriver
browser_options = Options()  
browser_options.add_argument("--headless")  
browser = webdriver.Chrome(options=browser_options)

# maximize browser window to avoid possible issues with elements not visible
browser.maximize_window()

# Directing the browser to the defined url
browser.get(url)

actions = ActionChains(browser)

# click Countries hover menu in top nav bar
countries_menu = browser.find_element_by_xpath('/html/body/div[3]/header/div[3]/div/div[1]/ul/li[3]/a')
actions.move_to_element(countries_menu)
actions.click(countries_menu).perform()

# Click All Countries submenu in top nav bar
all_countries_menu = browser.find_element_by_xpath('/html/body/div[3]/header/div[3]/div/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/ul/li[1]/a')
actions.move_to_element(all_countries_menu).perform()
all_countries_menu.click()

# find Filter by region input box
filter_by_region = browser.find_element_by_xpath('/html/body/div[3]/section/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/span/span/input')

# type 'americas'
filter_by_region.send_keys('americas')

# wait until 'Region of Americas' is visible
try:
    WebDriverWait(browser,5).until(
        EC.presence_of_element_located((By.XPATH, '//ul[@id="filter-by-region_listbox" and @aria-hidden="false"]'))
    )
except NoSuchElementException:
    browser.quit()
    exit(1)

# send key down to select 'Region of Americas'
filter_by_region.send_keys(Keys.ARROW_DOWN)

# send key Enter
filter_by_region.send_keys(Keys.ENTER)

# Assert if 'United States of America' is on the page
text_to_search = 'United States of America'
assert text_to_search in browser.page_source,"'United States of America' not found on page"

#close browser
browser.quit()