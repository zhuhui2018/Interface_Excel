#encoding:utf-8

import requests
from utils.ParseExcel import *
from Config.PublicData import *
from GetRelyValue.get_rely import *
from utils.HttpClient import *
from Action.data_store import *
from Action.check_result import *
from Action.write_result import *

def main():
    parseE = ParseExcel()
    parseE.loadWorkBook(TestCase)
    #获取测试用例sheet对象
    sheetobj = parseE.getSheetByName(apiExcelName)
    #获取执行列对象
    activeList = parseE.getColumn(sheetobj,API_active)
    for id,col in enumerate(activeList[1:],2):
        if col.value.lower() == "y":
            apiRow = parseE.getRow(sheetobj,id)
            apiName = apiRow[API_apiName-1].value
            requestUrl = apiRow[API_requestUrl-1].value
            requestMethod = apiRow[API_requestMethod-1].value
            paramsType = apiRow[API_paramsType-1].value
            apiTestName = apiRow[API_apiTestCaseFileName-1].value
            apiActive = apiRow[API_active-1].value
            #切换至需要执行的case sheet
            caseObj = parseE.getSheetByName(apiTestName)
            caseActiveList = parseE.getColumn(caseObj,CASE_active)
            for cid,cols in enumerate(caseActiveList[1:],2):
                if cols.value.lower() == "y":
                    caseRow = parseE.getRow(caseObj,cid)
                    requestData = caseRow[CASE_requestData-1].value
                    relyData = caseRow[CASE_RelyData-1].value
                    responseData = caseRow[CASE_responseData-1].value
                    dataStore = caseRow[CASE_dataStore-1].value
                    checkPoint = caseRow[CASE_checkPoint-1].value
                    #判断是否需要做依赖处理
                    if relyData:
                        #需要做数据依赖处理
                        requestData = GetRelyValue.get(requestData,relyData)
                    else:
                        print("第%s个API的第%s条不需要做数据依赖处理" % (id - 1, cid - 1))
                        #此时是没有依赖数据存在并且requestdata为字符串格式的dict，需要先转换为dict类型
                    if (not isinstance(requestData,dict) and not isinstance(requestData,int)) and (requestData[0] == "{" and requestData[-1] == "}"):
                        requestData = eval(requestData)

                    # 处理完接口请求参数的依赖数据后，接下来就是发送请求并获取响应结果
                    response = HttpClient.request(requestUrl, requestMethod, paramsType, requestData)
                    if response.status_code == 200:
                        #获取接口的响应body
                        responseBody = response.json()

                        #接下来做数据依赖存储
                        if dataStore:
                            RelyDataStore.do(apiName,cid-1,requestData,responseBody,eval(dataStore))
                    if checkPoint:
                        errorKey = CheckResult.check(response.json(),eval(checkPoint))
                        #将测试结果写回excel
                        if errorKey:
                            write_result(parseE,caseObj,response.json(),str(errorKey),cid)
                        else:
                            write_result(parseE, caseObj, response.json(), rowNo=cid)









if __name__ == "__main__":
    main()