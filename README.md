#Interface_Excel 基于Excel的接口测试框架

核心思想
用于接口自动化框架的分层结构
表现层（日志展示）---》业务层（发送请求）---》工具层（加密算法等）----》数据层（Excel，MySQL）

Action包

check_result.py ----检测接口返回的内容是否正确 
data_store.py ----数据依赖存储 
write_result.py ----写入响应数据，测试结果和错误信息

GetRelyValue包
get_rely  ----处理接口需要依赖上一个接口的数据，用于返回真实的可以发送请求的resquestBody

Config包 
public_data.py ----存放公共变量和接口需要依赖上一个接口返回的数据的结构模型

TestData 存放测试用例excel

Util包 
ParseExcel.py ----解析操作Excel，获取信息，写入信息 HttpClient.py ----发送http请求

runTest.py  ----主程序