from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Library import ConfigLibrary
from  selenium.webdriver.common.alert import  Alert
# import screenshot

path=r"/Users/kavyavijay/Desktop/untitled folder/chromedriver"

driver=Chrome()
# driver.get(ConfigLibrary.readData('Details','url'))
driver.get('https://www.thetestingworld.com/testings/')
driver.maximize_window()
driver.implicitly_wait(20)
text=driver.find_element('xpath','/html/body/header/h1/span').text
print(text)
text1=driver.find_element('xpath','/html/body/header/h1/span').is_enabled()
print(text1)
driver.find_element("xpath",ConfigLibrary.readData('Elements','user')).send_keys("karthik")
driver.find_element("xpath",'//*[@id="tab-content1"]/form/input[3]').send_keys("karthik@gmmail.com")
driver.find_element("xpath",'//*[@id="tab-content1"]/form/input[4]').send_keys('Qwertyu123@')
driver.find_element("xpath",'//*[@id="tab-content1"]/form/input[5]').send_keys('Qwertyu123@')
driver.find_element("xpath",'//*[@id="datepicker"]').send_keys('10/16/2023')
driver.find_element('xpath',"//i[@class='fa fa-calendar-o fa-2x']").click()
Act=ActionChains(driver)
wait= WebDriverWait(driver,10)

# Act.key_down()
# Act.send_keys(Keys.TAB).perform()
# sleep(3)
driver.find_element("xpath",'//*[@id="tab-content1"]/form/input[7]').send_keys('8892146902')
driver.find_element('xpath','//*[@id="tab-content1"]/form/input[8]').send_keys('abc')
sleep(4)
text2=wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="tab-content1"]/form/input[10]')))
text2.click()
print(text2)
# driver.find_element('xpath','//*[@id="tab-content1"]/form/input[10]').click()
gender=Select(driver.find_element('xpath','//*[@id="tab-content1"]/form/select[1]'))
gender.select_by_visible_text('Male')
Country=Select(driver.find_element('xpath','//*[@id="countryId"]'))
Country.select_by_visible_text('India')
state=Select(driver.find_element('xpath','//*[@id="stateId"]'))
state.select_by_visible_text('Karnataka')
city=Select(driver.find_element('xpath','//*[@id="cityId"]'))
city.select_by_visible_text('Bengaluru')
scroll=driver.find_element('xpath','//*[@id="cityId"]')
driver.execute_script('arguments[0].scrollIntoView(true);',scroll)
driver.find_element('xpath','//input[@placeholder="Zip code"]').send_keys('560036')
driver.execute_script("window.scrollBy(0,-500)")
driver.execute_script("window.scrollBy(0,500)")
driver.find_element('xpath','//*[@id="tab-content1"]/form/div/input[1]').click()
driver.find_element('xpath','//*[@id="tab-content1"]/form/div/input[2]').click()
# screenshot.takeScreenshot(driver,'karthik')
driver.quit()
# x=driver.window_handles
# for i in x:
#     driver.switch_to.window(i)
#     if i=='':
#         pass
#     else:
#         driver.close()

