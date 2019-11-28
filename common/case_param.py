import xlrd,os
from xlutils import copy
from.log import atp_log
from.setting import bases

class OpExcel():
    """从excel中读取参数，并转换成字典"""

    def get_param(self,param_path = os.path.join(bases.PARAM_PATH, bases.PARAM_NAME)):
        params = []
        if param_path.endswith('.xls') or param_path.endswith('.xlsx'):   #判断参数文件是否合法
            try:
                book = xlrd.open_workbook(param_path)   #打开excel
                sheet = book.sheet_by_index(0)      #获取第一个sheet页
                for i in range(1,sheet.nrows):      #循环每一行
                    row_data = sheet.row_values(i)      #获取每行数据
                    params.append(row_data[5:9])        #获取excel中6-9列的数据添加进param
            except Exception as e:
                atp_log.error('【%s】excel参数获取失败，错误信息为%s'%(param_path,e))
        else:
            atp_log.error('参数文件不合法>>%s'%param_path)
        return params


    def get_param_dic(self,params):
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

opexcel = OpExcel() #实例化


