#encoding:utf-8
from Config.PublicData import RESPONSE_DATA,REQUEST_DATA


class GetRelyValue(object):
    #用于获取接口的依赖数据
    def __init__(self):
        pass

    @classmethod
    def get(cls,requestData,relyData):
        #需要获取的数据可能来自上一个接口的请求参数，也可能来自响应body
        if not requestData or not relyData:
            return
        reData = requestData
        try:
            reData=eval(requestData)
        except SyntaxError as err:
            pass

        if relyData:
            relyData=eval(relyData)

        if isinstance(reData,dict):
            for key,value in relyData.items():
                if key == "request":
                    for k,v in value.items():
                        interfaceName,caseId = v.split("->")
                        val = REQUEST_DATA[interfaceName][caseId][k]
                        reData[k]=val
                elif key == "response":
                    for k,v in value.items():
                        interfaceName,caseId = v.split("->")
                        #val为公共变量中实际取的值
                        val = RESPONSE_DATA[interfaceName][caseId][k]
                        reData[k] = val
            return reData
        else:
            #说明请求是字符串，需要把字符串分割然后赋值
            k_v_str = requestData.split("&")
            k_v_dict = {}
            for i in k_v_str:
                k,v = i.split("=")
                k_v_dict[k]=v
            for key, value in relyData.items():
                if key == "request":
                    for k, v in value.items():
                        interfaceName, caseId = v.split("->")
                        val = REQUEST_DATA[interfaceName][caseId][k]
                        k_v_dict[k] = val
                elif key == "response":
                    for k, v in value.items():
                        interfaceName, caseId = v.split("->")
                        # val为公共变量中实际取的值
                        val = RESPONSE_DATA[interfaceName][caseId][k]
                        k_v_dict[k] = val
            requestStr = ""
            for k,v in k_v_dict.items():
                requestStr += k + "=" + v + "&"
            return requestStr[:-1]



if __name__ == "__main__":
    requestData = '{"username":"","password":""}'
    #requestData = "username=zhuhui&password=zhuhui11"
    relyData='{"request":{"username":"register->1","password":"register->1"}}'
    print(GetRelyValue.get(requestData, relyData))




