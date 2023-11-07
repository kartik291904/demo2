from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.mark.sanity
def test_valid():
    driver=Chrome()
    driver.get("https://iq.opengenus.org/range-len-1-python/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    text=driver.find_element("xpath","//h1[normalize-space()='Range len-1 in Python']").get_attribute('class')
    print(text)
