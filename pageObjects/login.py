from utilities.objUtil import objUtil

class login():

    userName={"loc" :"name", "att" : "userName"}
    password= {"loc" : "name" , "att": "password"}
    submit= {"loc" :"xpath" , "att" : "//input[@name='submit']"}

    def __init__(self,driver):
        self.driver=driver

    def textUserName(self):
        return objUtil.getObject(self.driver, self.userName)

    def textPassword(self):
        return objUtil.getObject(self.driver, self.password)

    def btnBubmit(self):
        return objUtil.getObject(self.driver, self.submit)
