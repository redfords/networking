from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# install selenium and webdriver
# sudo apt install firefox-geckodriver

# create the instance of firefox webdriver
driver = webdriver.Firefox()

# driver.get navigates to a page given by the url
driver.get("http://www.python.org")

# confirm that title has the word "Python" in it
assert "Python" in driver.title

# find element by the name attribute
# <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">
elem = driver.find_element(By.NAME, "q")

# start sending keys as in keyboard
# first we clear the input field
elem.clear()

# then we type and hit enter
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# to ensure that some results are found, make an assertion
assert "No results found." not in driver.page_source

# close the browser window, use quit to close all tabs
sleep(5)
driver.close()