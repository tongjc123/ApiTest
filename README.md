ApiTest框架

基本结构：

![image-20200401134808996](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401134808996.png)



本框架基于unittest,综合了很多大神的思想和实现方式。也有一点点自己不成熟的思考。python水平有限，槽点肯定很多，还有很多可优化封装的地方，暂时先用着吧，下个版本继续优化。

第一版本

1.Excel读取

将Excel数据转换为以表头为key，对应的每一个单元格为value的dict,并将多个dict组装到list。

![image-20200401135826080](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401135826080.png)

得到list[dict{}],即List<Map<K,V>>

![image-20200401140227046](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401140227046.png)

2.根据用例名称对应，手写case

```python
    def test_login_fail(cls):
        u"""登录失败场景"""
        atp_log.info('==========测试账号密码错误登录失败场景==========')
        test_login_fail_data = opexcel.get_test_data(opexcel.get_param("LoginCase"),
                                                     "test_login_fail")  #
        if not test_login_fail_data:
            atp_log.warning("未获取到用例数据")
        url = test_login_fail_data.get('url')
        atp_log.info("读取URL--【%s】" % url)
        headers = test_login_fail_data.get('headers')
        data = test_login_fail_data.get('data')
        atp_log.info("接口参数--【%s】" % data)
        expect_res = test_login_fail_data.get('expect_res')
        res = cls.s.post(url =url,
                        headers = json.loads(headers),
                        json=json.loads(data),
                        verify = False)
        result = json.loads(res.text)["msg"]
        #se2 = "用户名或密码错误121" #账户或密码错误则返回错误data
        atp_log.info('断言：【%s】？=【%s】' % (expect_res, result))
        cls.assertEqual(expect_res,result)
```

3.测试报告

![image-20200401141643275](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401141643275.png)

第二版本

1.日志模块

![image-20200401141314280](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401141314280.png)

2.邮件模块

![image-20200401141438315](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401141438315.png)

![image-20200401141527719](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401141527719.png)

3.setting模块

将全局的path,邮箱配置，参数配置封装

第三版本

1.DDT驱动

```python
@ddt.ddt
class NewLoginCase(MyBase):    
    params = opexcel.convert_data("LoginCase")    
    @ddt.data(*params)    
    def test_run_case(cls,i):        
        result_dict = opexcel.result_dict   #全局字典        
        if i['run'].lower() == 'yes':            #准备请求参数            
            url = i['url']            
            method = i['method'].lower()            
            data = i['data']            
            expect = i['expect']            
            row = int(i['id'].split('-')[1])  #当前用例在excel中的行数            
            #获取参数依赖            
            if i['depend_id'].startswith("smartpig"):                
                try:                    
                    depend_data = 
                  opexcel.get_response_data(result_dict[i['depend_id']],i['depend_data']) #获取依赖的返回数据                    
                	if method == 'delete':                        
                    	url = os.path.join(url, depend_data) #将url拼接                    					else:                        
                        data = data.replace('$',depend_data)  #如果是json中的依赖参数，就替换                 except Exception as e:                    
                    atp_log.error("获取返回依赖数据失败--%s"%e)            
            result = myRequest.run_main(method, url, data)            			 					result_dict[i['id']] = result #将返回结果添加到全局字典            
            print(result_dict)            
            cls.assertIn(expect, result)            
            try:                
                if expect in result:                    			  										cls.writeResult.writeresult(row, "测试通过")                
                else:                    
                    cls.writeResult.writeresult(row, "测试失败")            
                except Exception as e:                
                    atp_log("测试结果写入失败！！")
```

2.api参数关联问题处理

![image-20200401142658967](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401142658967.png)

引入jsonpath

根据depend_id找到对应的用例编号，根据用例编号找到对应的全局的result_dict，从中取出该api返回结果。根据depend_data,通过jsonpath，找到对应数据。

然后将对应数据赋值给relation_data里对应的字段。思考，如果是一个接口请求参数需要前面多个返回值的支持，那就将depend_id和depand_data做成List,如果list长度==1，则直接都去list[0],与之前操作一样。如果是list长度>=2,就循环list,分别取值，替换即可。

3.json文件

如果将我们接口所需参数直接贴至excel，会占用很大篇幅且很难看

使用json文件，与对应data字段对应，则清晰明了

![image-20200401143559087](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401143559087.png)

4.requests封装

根据不同的请求，get、post、delete、put等统一封装，调用一个方法即可

第四版本

1.测试结果回写

可以直观的通过excel，知道每一个api测试结果

![image-20200401143949081](C:\Users\jctong\AppData\Roaming\Typora\typora-user-images\image-20200401143949081.png)