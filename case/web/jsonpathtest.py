#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : jsonpathtest.py
# Author: TongJC
# Date  : 2020-03-31
import jsonpath
import json

json_str = '{"success":true,"msg":"成功","data":{"page":1,"totalPage":1,"totalCount":3,"canAdd":true,"list":[{"uid":"ac711775-7324-11ea-bd3a-44a8421c2cd6","companyId":"5f8e8bcc-c077-46f5-a6ae-d9cfa28bb763","companyName":"夏津新希望六和农牧有限公司","farmId":"402376dd-0036-11ea-bd3a-44a8421c2cd6","farmName":"夏津四场一线","docNo":"1070P3200331002","supplierId":"184b4f3d-aeb2-11e9-b1aa-c81fbe72939c","supplierName":"高密六和养殖有限公司","planDate":1585584000000,"planQuantity":10,"receiveQuantity":0,"status":"done","statusName":"已完成","receiveStatus":"not_receive","receiveStatusName":"未接收","planType":null,"createMan":"4b7e1f79-06b0-11ea-bd3a-44a8421c2cd6","remarks":"","dataStatus":"normal","canEdit":true},{"uid":"5deb7c2e-732c-11ea-bd3a-44a8421c2cd6","companyId":"5f8e8bcc-c077-46f5-a6ae-d9cfa28bb763","companyName":"夏津新希望六和农牧有限公司","farmId":"402376dd-0036-11ea-bd3a-44a8421c2cd6","farmName":"夏津四场一线","docNo":"1070P3200331003","supplierId":"184b4f3d-aeb2-11e9-b1aa-c81fbe72939c","supplierName":"高密六和养殖有限公司","planDate":1585584000000,"planQuantity":10,"receiveQuantity":0,"status":"done","statusName":"已完成","receiveStatus":"not_receive","receiveStatusName":"未接收","planType":null,"createMan":"4b7e1f79-06b0-11ea-bd3a-44a8421c2cd6","remarks":"","dataStatus":"normal","canEdit":true},{"uid":"874895d1-7300-11ea-bd3a-44a8421c2cd6","companyId":"5f8e8bcc-c077-46f5-a6ae-d9cfa28bb763","companyName":"夏津新希望六和农牧有限公司","farmId":"402376dd-0036-11ea-bd3a-44a8421c2cd6","farmName":"夏津四场一线","docNo":"1070P3200331001","supplierId":"184b4f3d-aeb2-11e9-b1aa-c81fbe72939c","supplierName":"高密六和养殖有限公司","planDate":1585584000000,"planQuantity":10,"receiveQuantity":0,"status":"done","statusName":"已完成","receiveStatus":"not_receive","receiveStatusName":"未接收","planType":null,"createMan":"4b7e1f79-06b0-11ea-bd3a-44a8421c2cd6","remarks":"","dataStatus":"normal","canEdit":true}]},"code":"SUCCESS"}'
pyjson = json.loads(json_str)

mse = jsonpath.jsonpath(pyjson,'$.data.list[0].docNo')
print(type(mse))
print(mse)

cell = int("smart-001".split('-')[1])
print(cell)