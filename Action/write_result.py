from utils.ParseExcel import *
from Config.PublicData import *

def write_result(wbObj,sheetObj,responseBody,errorKey=None,rowNo=None):
    #将测试结果写入到excel对应的单元格中

    #写响应body
    wbObj.writeCell(sheetObj, content = "%s" %responseBody,rowNo = rowNo, colsNo = CASE_responseData)

    #写校验结果状态列及错误信息列
    if errorKey:
        wbObj.writeCell(sheetObj,content= "fail",rowNo=rowNo,colsNo=CASE_status)
        wbObj.writeCell(sheetObj,content = "%s" % errorKey,rowNo=rowNo,colsNo=CASE_errorInfo)
    else:
        wbObj.writeCell(sheetObj, content="pass", rowNo=rowNo, colsNo=CASE_status)