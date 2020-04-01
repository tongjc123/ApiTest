import xlrd,os,json
import jsonpath
from xlutils import copy
from common.log import atp_log
from common.setting import bases

class OpExcel():
    """从excel中读取参数，并转换 成字典"""
    def __init__(self):
        # 用一个字典来接收每个请求返回的数据，作为后面有参数关联的全局参数
        self.result_dict = {}
    #从excel提取list[dict{}]
    def get_param(self,sheet_name):
        param_path = os.path.join(bases.PARAM_PATH, bases.PARAM_NAME)
        params_list = []
        if param_path.endswith('.xls') or param_path.endswith('.xlsx'):   #判断参数文件是否合法
            try:
                book = xlrd.open_workbook(param_path)   #打开excel
                sheet = book.sheet_by_name(sheet_name)      #获取sheet页
                title = sheet.row_values(0)
                for i in range(1,sheet.nrows):      #循环每一行
                    row_data = sheet.row_values(i)      #获取每行数据
                    data = dict(zip(title,row_data))    #将第标题和对应数据组装成dict
                    params_list.append(data)

            except Exception as e:
                atp_log.error('【%s】excel参数获取失败，错误信息为%s'%(param_path,e))
        else:
            atp_log.error('参数文件不合法>>%s'%param_path)

        return params_list

    """
        def get_test_data(self,params):
        param_list = []
        param_dic = {}
        dic_id = 1
        for list in params:
            case_num =len(params)
            for i in list:
                param_list.append(i)      #循环取出params中的参数append到param_list
                if i.endswith("}"):        #从param_list中取出参数，组装成字典，key从1开始计数
                    param_dic[dic_id] = eval(i)        #如果取出的参数是｛｝这种形式的str，使用eval处理为有效表达式dict
                else:
                    param_dic[dic_id] = i
                dic_id += 1
        atp_log.info("共获取到%s条用例参数"%case_num)
        return param_dic
    """
    def get_test_data(self,params_list,case_name):
        #本方法暂时没用
        for case_data in params_list:
            if case_name == case_data['case_name']: #当从列表中找到对应用例名的数据时，返回该字典
                return case_data

    #获取json中参数
    def get_json_data(self,keyname):
        json_path = os.path.join(bases.PARAM_PATH,"data.json")
        with open(json_path) as f:
            data = json.loads(f.read())[keyname]  #读取对应的json参数
        return data

    #多个依赖参数分割
    def relation_data(self,str):
        list_data = []
        if str !='':
            if ',' in str:
                list_data = str.split(',')
            else:
                list_data.append(str)
        return list_data

    #将读取到的参数进行处理
    def convert_data(self,sheet):
        data = self.get_param(sheet)
        for i in data:
            if i['data'] != '':
                if i['data'].endswith('}'):  #如果以｝结尾，表示本身是json参数
                    i['data'] = json.loads(i['data'])   #本身是json，直接转换为字典即可
                try:
                    i['data'] =self.get_json_data(i['data'])   #否则就取json文件中对应的json
                except:
                    atp_log.info("不需从json文件取数据")
        return data

    #关联参数提取
    def get_response_data(self,str, regex):
        if str !='' and regex !='':
            pyjson = json.loads(str)   #返回参数的json字串转换为dict
            data =jsonpath.jsonpath(pyjson,regex)  #根据jsonpath表达式查找对应数据
            if isinstance(data,list):
                return data[0]  #jsonpath提取返回结果为list
            else:
                atp_log.error('关联参数获取为None')
                return ''
        else:
            atp_log.info('返回参数为空或Excel中depend_data为空')


opexcel = OpExcel() #实例化

if __name__ == '__main__':
    import requests
    # params=opexcel.convert_data("LoginCase")
    # req = requests.session()
    # req.post(url =params[0]['url'],json = params[0]['data'])
    # res = req.post(url =params[2]['url'] ,headers = {'RSESSIONID_NAME':'82f8192546aa5d5b4a3099e8361ec525'},json = params[2]['data'])
    # print(res.text)

    #print(opexcel.get_param("LoginCase"))

    print(opexcel.relation_data('smaaa,hshha'))




