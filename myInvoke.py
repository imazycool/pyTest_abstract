# content of myinvoke.py
import pytest
import sys
import os

#os.getcwd().replace("\\testCases","") +"\\config\\chromedriver.exe"
# class MyPlugin:
#     def pytest_sessionfinish(self):
#         print("*** test run reporting finishing")
#
#
if __name__ == "__main__":
    path = "pytest testCases/test_login.py"
    print(path)
    # pytest.main()
    pytest.main(['-q', '-s', "testCases/test_login.py","--html=report.html" , "-n 3"] )