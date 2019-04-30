# # -*- coding: utf-8 -*-
# import pandas as pd
# #from bs4 import BeautifulSoup
# import urllib.request as req
# import urllib.parse
# import re
# import json
# import sys
# import time
# import random
#
# print(sys.getdefaultencoding())
#
# class LagouCrawler:
#
#     def __init__(self,location_word,position_word,pages):
#         self.location_word = location_word
#         self.position_word = position_word
#         self.pages = pages
#         self.location_url = 'https://www.lagou.com/jobs/positionAjax.json?city=%s&needAddtionalResult=false'#positionAjax.json?city=北京&needAddtionalResult=false
#
#     def request_method(self,params):
#         #伪装浏览器，打开网站
#         headers = {
#             'Connection': 'Keep-Alive',
#             'Accept': 'text/html, application/xhtml+xml, */*',
#             'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
#             'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
#             'Host':'www.lagou.com',
#             'Origin':'https://www.lagou.com',
#         }
#         url = self.location_url%urllib.parse.quote(self.location_word)
#         params_post = urllib.parse.urlencode(params).encode()
#         print(params_post)
#         reqs = req.Request(url,data=params_post,headers=headers,method='POST')
#         return reqs
#
#     def lagou_search(self,page_num=1):
#         #抓取数据
#         if(page_num == 1):
#             first_flag = 'true'
#         else:
#             first_flag = 'false'
#         params = {
#             'first':first_flag,
#             'kd':self.position_word,
#             'pn':page_num
#         }
#         request_m = self.request_method(params)
#
#         conn = req.urlopen(request_m)
#         return_str = conn.read().decode()
#         return json.loads(return_str)
#     def save_csv(self,df,p):
#         # 保存文件
#         df.to_csv(path_or_buf = 'd:\\xxx\\lagou\\lagou_%d.csv'%p,encoding='gbk')
#
#     def crawler(self):
#         # 把抓取的数据存入CSV文件，设置时间间隔，以免被屏蔽
#         dfs = []
#         for p in range(self.pages+1):
#             tmp_list = []
#             if(p == 0):
#                 continue
#             json_info = self.lagou_search(page_num=p)
#             json_content = json_info['content']
#             position_result = json_content['positionResult']['result']
#
#             for row in position_result:
#                 tmp_list.append([row['positionName'],row['workYear'],row['education'],row['financeStage'],row['companyShortName'],row['industryField'], \
#                                  row['city'],row['salary'],row['positionId'],row['positionAdvantage'],row['district'],','.join(row['positionLables']), \
#                                  ','.join(row['companyLabelList']),row['companySize'],row['companyFullName']])
#             df = pd.DataFrame(tmp_list,columns=['position_name','work_year','education','finance_stage','company_short_name','industry_field', \
#                                                 'city','salary','position_id','position_advantage','district','position_lables', \
#                                                 'company_label_list','company_size','company_full_name'])
#             dfs.append(df)
#             print(df.head())
#             self.save_csv(df,p)
#             time.sleep(random.randint(41,92))
#         final_df = pd.concat(dfs,ignore_index=True)
#         self.save_csv(final_df,0)
#
# def lagou():
#     pages = 30
#     location_word = '北京'
#     position_word = '数据分析师'
#     lg = LagouCrawler(location_word,position_word,pages)
#     lg.crawler()
#
