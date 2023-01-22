import pytest
from utilities.getData import getData
from pageObjects.login import login
import pandas as pd
import os
import json


def getUserData():
    dataList = pd.read_csv(os.getcwd().replace("\\testCases", "") + "\\testData\\userData.csv")
    # print (dataList["data1"], dataList["data2"])
    return (dataList["data1"], dataList["data2"])
    # return (dataList["data1"])


def test_verifyPageTitle(driver):
    act_titile = driver.title
    driver.close()
    print("hello test----> ", act_titile)


@pytest.mark.parametrize('user_data', getUserData())
def test_verifyPageLogin_(driver, user_data):
    lg = login(driver)
    url=driver.current_url
    print(user_data.to_dict())
    lg.textUserName().send_keys(user_data[0])
    lg.textPassword().send_keys(user_data[1])
    lg.btnBubmit().click()


def test_verifyPageLogin(driver):
    lg = login(driver)
    url=driver.current_url
    td=(getData.getTestData())
    print(td)
    lg.textUserName().send_keys(td.get("userName"))
    lg.textPassword().send_keys(td.get("password"))
    lg.btnBubmit().click()





