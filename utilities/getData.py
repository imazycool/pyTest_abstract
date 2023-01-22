import pytest
import pandas as pd
import os



class getData():

    def getUserData():
        dataList = pd.read_csv(os.getcwd().replace("\\testCases", "") + "\\testData\\userData.csv")
        # # dataList = list(dataList)
        # print(dataList.to_dict())
        # ds=json.dumps(dataList.to_dict(),indent = 4)
        # return ds


    def getTestData():
        testName = (os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])
        print(testName)
        path = os.getcwd().replace("\\testCases", "") + "\\testData\\testData.csv"
        testData = pd.read_csv(path)
        testData = testData.loc[testData['testCaseName']==testName]
        numberofTests=len(testData)
        if numberofTests==0:
            return None
        else :
            dataFileFlag=testData['dataFile'][numberofTests-1]
            print(dataFileFlag)
            return testData

