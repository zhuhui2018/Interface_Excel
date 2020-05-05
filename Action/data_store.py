from Config.PublicData import RESPONSE_DATA,REQUEST_DATA

class RelyDataStore(object):
    def __init__(self):
        pass

    @classmethod
    def do(cls,apiName,caseId,requestData,responseBody,datastore):
        if isinstance(requestData, str):
            param_dict = {}
            k_v_str = requestData.split("&")
            for i in k_v_str:
                k,v = i.split("=")
                param_dict[k]=v
            requestData = param_dict

        for key,value in datastore.items():
            if key == "request":
                #说明需要存储的数据来自接口的请求参数
                for i in value:  #i指的是username，password
                    if i in requestData:
                        if apiName not in REQUEST_DATA:
                            REQUEST_DATA[apiName] = {str(caseId):{i : requestData[i]}}
                        else:
                            if str(caseId) in REQUEST_DATA[apiName]:
                                REQUEST_DATA[apiName][str(caseId)][i] = requestData[i]
                            else:
                                REQUEST_DATA[apiName][str(caseId)] = {i:requestData[i]}
                    else:
                        print("需要做数据依赖存储的参数%s不存在" %i)
            if key == "response":
                for j in value:
                    if j in responseBody:
                        if apiName not in RESPONSE_DATA:
                            RESPONSE_DATA[apiName] = {str(caseId):{j : responseBody[j]}}
                        else:
                            if str(caseId) in RESPONSE_DATA[apiName]:
                                RESPONSE_DATA[apiName][str(caseId)][j] = responseBody[j]
                            else:
                                RESPONSE_DATA[apiName][str(caseId)] = {j:responseBody[j]}
                    else:
                        print("需要做数据依赖存储的参数%s不存在" % j)
                print(RESPONSE_DATA,REQUEST_DATA)

if __name__ == "__main__":
    #requestData = {"username":"srsdcx35","password":"wcx19wac1"}
    requestData = "username=zhuhui11&password=xdefedrf&flag=true"
    responseBody = {'username': 'srsdcx35', 'code': '01'}
    datastore = {"request":["username","password"],"response":["code"]}
    print(RelyDataStore.do("register",1,requestData,responseBody,datastore))



