import xlrd,os
from xlutils import copy
from common.log import atp_log
from common.setting import bases

class OpExcel():
    """从excel中读取参数，并转换成字典"""

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
                    data = dict(zip(title,row_data))    #讲第标题和对应数据组装成dict
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

        for case_data in params_list:
            if case_name == case_data['case_name']: #当从列表中找到对应case_name的数据时，返回该字典
                return(case_data)



opexcel = OpExcel() #实例化




