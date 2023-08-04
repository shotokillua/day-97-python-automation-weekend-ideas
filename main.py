import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

import random

chromedriver_autoinstaller.install()

chrome_driver_path = "D:\Development\chromedriver.exe" # make sure you update this with the most current version of Chrome to work

options = webdriver.ChromeOptions() # this allows you to set options such as enabling headless mode or customize other behaviors of the Chrome browser
options.add_experimental_option("detach", True) # this will keep the browser window open after the webdriver is closed - good for troubleshooting

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)

search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.click()
search.send_keys('Ideas to do this weekend')
search.send_keys(Keys.ENTER)

driver.implicitly_wait(2)

for_couples = driver.find_element(By.XPATH, '//*[@id="bqHHPb"]/div/div/a[1]')
for_couples.click()

driver.implicitly_wait(2)

link = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/a')
link.click()

driver.implicitly_wait(2)

ideas = driver.find_elements(By.TAG_NAME, 'h3')
list_of_ideas = []
for idea in ideas:
    list_of_ideas.append(idea.text)

# print(list_of_ideas)
refined_ideas_list = list_of_ideas[:29]
# print(refined_ideas_list)
print(random.choice(refined_ideas_list))