from selenium import webdriver
import pickle
import re
import os

class WebscrappingIncentivos():
    def set_firefox_profile(self, download_dir):
        profile = webdriver.FirefoxProfile()
