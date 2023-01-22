import selenium
from selenium.webdriver.common.by import By


class objUtil:


    def getObject(driver, objText):
        if type(objText) is not dict:
            kw_txt="xpath"
            ele_txt=objText
        else:
            kw_txt=objText.get("loc")
            ele_txt= objText.get("att")
        match kw_txt:
            case "name":
                element = driver.find_element(By.NAME, ele_txt)
            case "id":
                element = driver.find_element(By.ID, ele_txt)
            case "xpath":
                element = driver.find_element(By.XPATH, ele_txt)
            case default :
                element = driver.find_element(By.XPATH, ele_txt)

        return element
