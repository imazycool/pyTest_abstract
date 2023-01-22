from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities.config import readConfig
import pytest
import os
import pandas as pd
from utilities.getData import getData

@pytest.fixture()
def driver():
    path = os.getcwd().replace("\\testCases","") +"\\config\\chromedriver.exe"
    print("path to driver --> ", path)
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    # implicitly_wait(30).install()
    driver.implicitly_wait(30)
    driver.get(readConfig.getBase_url())
    driver.maximize_window()
    return driver




