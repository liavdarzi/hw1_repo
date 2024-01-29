from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import webdriver_manager
import time

#ex1
#chrome_path ="C:\Program Files\Google\Chrome\Application\chrome.exe"
#url = 'https://translate.google.co.il/?hl=iw&sl=iw&tl=en&op=translate'
#driver = webdriver.Chrome()
#driver.get(url)
#1b
# mozile_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
#driver2 = webdriver.Firefox()
#driver2.get(url)

#2
# time.sleep(5)
# title = driver.title
# driver.refresh()
# if title == driver.title:
#     print("equal")
# driver.close()

#ex3
#translator = driver.find_element(By.XPATH,"/html/body[@id='yDmH0d']/c-wiz[@class='zQTmif SSPGKf kXN2zb BIdYQ']/div[@class='T4LgNb']/div[@class='ToWKne']/c-wiz[@class='MOkH4e iYelWb yF6Zo ']/div[@class='OlSOob']/c-wiz[@class='QsA0jb']/div[@class='ccvoYb EjH7wc']/div[@class='AxqVh']/div[@class='OPPzxe']/c-wiz[@class='rm1UF UnxENd']/span/span/div[@class='QFw9Te']/textarea[@class='er8xn']")
#time.sleep(5)
#translator.send_keys("מלך")

#ex5
# driver = webdriver.Chrome()
# url= "https://www.youtube.com/"
# driver.get(url)
# youtube = driver.find_element("name",'search_query')
# youtube.send_keys("חייל מלבנון")
# driver.find_element(By.ID,'search-icon-legacy').click()

# url = "https://translate.google.com/"
# driver.get(url)
# locat1 = driver.find_element(By.XPATH,"/html/body[@id='yDmH0d']/c-wiz[@class='zQTmif SSPGKf kXN2zb BIdYQ']/div[@class='T4LgNb']/div[@class='ToWKne']/c-wiz[@class='MOkH4e iYelWb yF6Zo ']/div[@class='OlSOob']/c-wiz[@class='QsA0jb']/div[@class='ccvoYb EjH7wc']/div[@class='AxqVh']/div[@class='OPPzxe']/c-wiz[@class='rm1UF UnxENd']/span/span/div[@class='QFw9Te']/textarea[@class='er8xn']").send_keys("one location")
# # locat2 = driver.find_element(By.XPATH,"/html/body[@id='yDmH0d']/c-wiz[@class='zQTmif SSPGKf kXN2zb BIdYQ']/div[@class='T4LgNb']/div[@class='ToWKne']/c-wiz[@class='MOkH4e iYelWb yF6Zo']/div[@class='OlSOob']/c-wiz[@class='QsA0jb']/div[@class='ccvoYb EjH7wc']/div[@class='AxqVh']/div[@class='OPPzxe']/c-wiz[@class='rm1UF UnxENd']").send_keys("two")
# b = driver.find_element(By.NAME, "jfk-button").send_keys("two location")
# c = driver.find_element(By.XPATH, "//input[@type=‘submit']").send_keys("three location")
# # locat3 = driver.find_element(By.XPATH,"/html/body[@id='yDmH0d']/c-wiz[@class='zQTmif SSPGKf kXN2zb BIdYQ']/div[@class='T4LgNb']/div[@class='ToWKne']/c-wiz[@class='MOkH4e iYelWb yF6Zo']/div[@class='OlSOob']/c-wiz[@class='QsA0jb']/div[@class='ccvoYb EjH7wc']/div[@class='AxqVh']/div[@class='OPPzxe']/c-wiz[@class='rm1UF UnxENd']/div[@class='UdTY9 leDWne']/div[@class='kO6q6e']").send_keys("three")
# input()

#ex7
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# login = driver.find_element(By.ID,'email')
# login.send_keys("darziliav@walla.com")
# login = driver.find_element(By.ID,'pass')
# login.send_keys("liav10420031491999")
# login = driver.find_element(By.TAG_NAME,"button")
# login.click()
# input()

#ex8
# driver = webdriver.Chrome()
# driver.get("https://www.google.co.uk/")
# driver.delete_all_cookies()
# coockies = driver.get_cookies()
# print(coockies)

#ex9
driver = webdriver.Chrome()
driver.get("https://github.com/")
githab = driver.find_element(By.CLASS_NAME,'header-search-button').click()
githab = driver.find_element(By.ID,'query-builder-test').send_keys("Selenium")
githab = driver.find_element(By.XPATH,"/html/body[@class='logged-out env-production page-responsive header-overlay home-campaign intent-mouse']/div[@class='logged-out env-production page-responsive header-overlay home-campaign']/div[@class='position-relative js-header-wrapper ']/header[@class='Header-old header-logged-out js-details-container Details position-relative f4 py-3']/div[@class=' d-flex flex-column flex-lg-row flex-items-center p-responsive height-full position-relative z-1']/div[@class='HeaderMenu--logged-out p-responsive height-fit position-lg-relative d-lg-flex flex-column flex-auto pt-7 pb-4 top-0']/div[@class='header-menu-wrapper d-flex flex-column flex-self-end flex-lg-row flex-justify-between flex-auto p-3 p-lg-0 rounded rounded-lg-0 mt-3 mt-lg-0']/div[@class='d-lg-flex flex-items-center mb-3 mb-lg-0 text-center text-lg-left ml-3']/qbsearch-input[@class='search-input expanded']/div[@class='search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center mr-4 rounded']/div/modal-dialog[@id='search-suggestions-dialog']/div[@class='Overlay-body Overlay-body--paddingNone']/div/div[@class='search-suggestions position-fixed width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container']/form[@id='query-builder-test-form']/query-builder[@id='query-builder-query-builder-test']/div[@class='FormControl FormControl--fullWidth']/div[@class='position-relative']/ul[@id='query-builder-test-results']/li[@class='ActionList-sectionDivider']/ul/li[@id='query-builder-test-result-selenium']/span[@class='ActionListContent ActionListContent--visual16 QueryBuilder-ListItem']/span[@class='ActionListItem-descriptionWrap']/span[@class='ActionListItem-label text-normal']")
githab.click()
input()