# -*- coding:utf-8 -*-

from util import constant,handle,crawl,io
from newseed.util import linkList
import math
import re
from bs4 import BeautifulSoup
from openpyxl import Workbook
import os
import time
import xlrd
import requests
import chardet
import json
import hashlib
import index
import jieba
from huxiu import crawl_original_data






# 4,5,8,10,11,16,20,32




print(7148-100-50-30)

# url = 'https://www.huxiu.com/article/19.html'
# print(crawl_original_data.getInfoFromHtml(url))




# test = """<div class="\"mod-b" mod-art\" data-aid="\"181424\"">
# 	\n\n
# 	<div class="\"mod-angle\"">
# 		热
# 	</div>
# 	\n
# 	<div class="\"mod-thumb\"">
# 		\n        <a class="\"transition\"" href="\"/article/181424.html\"" target="\"_blank\"" title="\"当人工智能都能下棋时，你还能做什么？我与一位创业中的博士聊了聊\"">\n            <img class="\"lazy\"" data-original="\"https://imgs.bipush.com/article/cover/201612/13/162813375721.jpg?imageView2/1/w/220/h/165/|imageMogr2/strip/interlace/1/quality/85/format/jpg\"" alt="\"当人工智能都能下棋时，你还能做什么？我与一位创业中的博士聊了聊\"">\n        </a>\n
# 	</div>
# 	\n                    <a href="\"/whatsnew.html\"" class="\"column-link\"" target="\"_blank\"">24小时</a>\n
# 	<div class="\"mob-ctt\"">
# 		\n
# 		<h2><a href="\"/article/181424.html\"" class="\"transition" msubstr-row2\" target="\"_blank\"">当人工智能都能下棋时，你还能做什么？我与一位创业中的博士聊了聊</a></h2>
# 		\n
# 		<div class="\"mob-author\"">
# 			\n
# 			<div class="\"author-face\"">
# 				\n                <a href="\"/member/1341581.html\"" target="\"_blank\""><img src="\"https://imgs.bipush.com/auth/data/avatar/001/34/15/81_avatar_big.jpg!40x40?|imageMogr2/strip/interlace/1/quality/85/format/jpg\""></a>\n
# 			</div>
# 			\n            <a href="\"/member/1341581.html\"" target="\"_blank\"">\n                <span class="\"author-name\"">天使不投资人</span>\n            </a>\n            <a href="\"/vip\"" target="\"_blank\""><i class="\"i-vip" icon-vip\"></i></a>\n            <i class="\"i-icon" icon-auth2\" title="\"虎嗅认证作者\""></i><span class="\"time\"">1天前</span>\n            <i class="\"icon" icon-cmt\"></i><em>18</em>\n            <i class="\"icon" icon-fvr\"></i><em>81</em>\n
# 		</div>
# 		\n        <!--外部文章/内部文章两者取其一-->\n
# 		<div class="\"mob-sub\"">
# 			世界对人工智能变得愈发宽容
# 		</div>
# 		\n
# 	</div>
# 	\n
# </div>
# \n
# <div class="\"mod-b" mod-art\" data-aid="\"181735\"">
# 	\n\n
# 	<div class="\"mod-angle\"">
# 		热
# 	</div>
# 	\n
# 	<div class="\"mod-thumb\"">
# 		\n        <a class="\"transition\"" href="\"/article/181735.html\"" target="\"_blank\"" title="\"微信付费阅读内测图流出，原来如此…\"">\n            <img class="\"lazy\"" data-original="\"https://imgs.bipush.com/article/cover/201702/18/234325556970.jpg?imageView2/1/w/220/h/165/|imageMogr2/strip/interlace/1/quality/85/format/jpg\"" alt="\"微信付费阅读内测图流出，原来如此…\"">\n        </a>\n
# 	</div>
# 	\n                    <a href="\"/whatsnew.html\"" class="\"column-link\"" target="\"_blank\"">24小时</a>\n
# 	<div class="\"mob-ctt\"">
# 		\n
# 		<h2><a href="\"/article/181735.html\"" class="\"transition" msubstr-row2\" target="\"_blank\"">微信付费阅读内测图流出，原来如此…</a></h2>
# 		\n
# 		<div class="\"mob-author\"">
# 			\n
# 			<div class="\"author-face\"">
# 				\n                <a href="\"/member/1538253.html\"" target="\"_blank\""><img src="\"https://imgs.bipush.com/auth/data/avatar/001/53/82/53_1478687916.jpg!40x40?|imageMogr2/strip/interlace/1/quality/85/format/jpg\""></a>\n
# 			</div>
# 			\n            <a href="\"/member/1538253.html\"" target="\"_blank\"">\n                <span class="\"author-name\"">这不科学啊</span>\n            </a>\n            <a href="\"/vip\"" target="\"_blank\""></a>\n                                    <span class="\"time\"">1天前</span>\n            <i class="\"icon" icon-cmt\"></i><em>7</em>\n            <i class="\"icon" icon-fvr\"></i><em>20</em>\n
# 		</div>
# 		\n        <!--外部文章/内部文章两者取其一-->\n
# 		<div class="\"mob-sub\"">
# 			在舆论热点的推动下，总会有人把去“挖坟”。
# 		</div>
# 		\n
# 	</div>
# 	\n
# </div>"""

# soup = BeautifulSoup(test)
# print(soup)
# resultList = soup.find_all('div',class_ = "mod-b mod-art")
# print(resultList)


# for i in range(5,-1,-1):
#     print(i)




# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
# url = "https://www.huxiu.com/v2_action/article_list"
# # 获取内容
# r = requests.get(url=url, headers=header)
# html = r.content.decode('utf-8')
# dic = json.loads(html)


# print('现在时间：',time.time())
# timeStamp = 1333426680  #2012-04-03 12:18:00
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timeStamp)))



# 虎嗅文章列表地址url
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
# url = 'https://www.huxiu.com/v2_action/article_list'
# data = {'huxiu_hash_code':'71c4da50b168c64a0d319bea4e368c8c','page': ''}
# data['page'] = 1111
#
# r = requests.post(url=url, data=data,headers=header)
# html = r.content.decode('utf-8')
# print(html)
# dicList = json.loads(html)
# print(dicList)














# totalpage 1112
# num 181836
# print(181836-(1112*30)) # 148476
# 148476
# 148470
# 148463
# 148450
# 148435
# 148400
# 148350
# 148300
# 148200
# 148000
# 147476






# filePath = index.ROOT_PATH + '/data/kr_data/origin_html_kr_201702171539.txt'
# fr = open(filePath,'r',encoding='utf-8')
# line = fr.readline()
# dic = json.loads(line.replace('\ufeff',''))
# cake = dic['data']['extraction_tags']
# breadList = json.loads(cake)
# print(breadList,type(breadList))
# for item in breadList:
#     print(item[0])









# timeStamp = '2016-08-04 21:22:49'
# print(timeStamp.split(' ')[0])




# startNum = 5064073
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
# url = "http://36kr.com/api/post/" + str(startNum) + "/next"
# # 获取内容
# r = requests.get(url=url, headers=header)
# html = r.content.decode('utf-8')
# print(html)





# class Node(object):
#     def __init__(self,val):
#         self.val = val
#         self.nextLink = None
#
# node = Node(4)
# print(node.val)






# a = lambda x,y:x+y
# print(a(3,4))
# sorted(swList, key= lambda a_entry : a_entry[1], reverse= True)

# testList = [['a',4],['c',1],['b',2]]
# print(sorted(testList,key= lambda item:item[1]))
# print(sorted(testList,key= lambda item:item[1],reverse=True))
# print(sorted(testList,key= lambda item:item[0]))




# time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
# print(time.time())
# print(time.localtime(time.time()))
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#
# ftime = '2017-02-17 11:09:51'
# print(time.mktime(time.strptime(ftime,'%Y-%m-%d %H:%M:%S')))
# print(time.mktime(time.strptime(ftime,'%Y-%m-%d %H:%M:%S')))

# ## 36kr 原始html提取数据
# filePath = index.ROOT_PATH + '/data/kr_data/origin_html_kr_201702151528.txt'
# fr = open(filePath,'r',encoding='utf-8')
# line = fr.readline()
# dic = json.loads(line.strip())
# print(dic['data']['title'])
# print(dic['data']['published_at'])
# print(dic['data']['currentUrl'])
# print(type(dic['data']['extraction_tags']),dic['data']['extraction_tags'])
# print(type(json.loads(dic['data']['extraction_tags'])),dic['data']['extraction_tags'])
# for item in json.loads(dic['data']['extraction_tags']):
#     print(item[0],item[1])
# print(dic['data']['user']['name'])



# timeStamp = '201702141130'
# print(time.strptime(timeStamp,'%Y%m%d%H%M'))



# test = "\u4e1d\u7ef8\u4e4b\u8def\u4e50\u56e2\u5728\u683c\u83b1\u7f8e\u201c\u6885\u5f00\u4e09\u5ea6\u201d\uff0c\u9664\u4e86\u611f\u8c22\u9a6c\u53cb\u53cb\uff0c\u4f60\u8fd8\u5e94\u8be5\u8ba4\u8bc6\u4e00\u4e0b\u5434\u5f64"
# print(test)
# print(test.encode('unicode_escape').decode('unicode_escape'))

# test = """加啊四系啊劳动法<a href="www.baidu.com"><img src="www.xxxx.xxx"></a>系啊觉得是客服<a href="www.ifanr.com">及阿娇事发</a>系啊李开复打扫房间就"""
# soup = BeautifulSoup(test)
# aTagList = soup.find_all('a')
# for item in aTagList:
#     print(type(item),item,item.string)
#     if item.string != None:
#         print(item.get('href'))







# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# # 使用python表示链表
# other2 = ListNode('8')
# three = ListNode('3')
# three.next = other2
# other = ListNode('8')
# other.next = three
# two = ListNode('2')
# two.next = other
# head = ListNode('1')
# head.next = two
#
#
# currentNode = head
# print(currentNode.val)
# while(currentNode.next != None):
#     currentNode = currentNode.next
#     print(currentNode.val)


#
# class Solution(object):
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
#         currentNode = head
#         headLink = None
#         while(currentNode.next != None):
#             if currentNode.val == val:


# test = "201702141536"
# print(time.mktime(time.strptime(test,'%Y%m%d%H%M')))
# print(type(time.mktime(time.strptime(test,'%Y%m%d%H%M'))))
# result = int(time.mktime(time.strptime(test,'%Y%m%d%H%M')))
# print(result)
# beforeDay = result - (1 * 24 * 60 * 60)
# print(beforeDay)
# print(time.strftime('%Y%m%d%H%M',time.localtime(beforeDay)))


# timeStamp = '201702141130'
# print(time.mktime(time.strptime(timeStamp,'%Y%m%d%H%M')))


# test = '12 天44前'
# result = re.findall('([0-9]+)',test,re.S)
# print(result)



# test = '201702141536'
# print(test[0:4])
# print(test[4:6])
# print(test[6:8])



# test = 'origin_html_pingwest_201701181122'
# print(test.split('_'))
# print(test.split('_')[len(test.split('_'))-1])



# print(time.strftime('%Y%m%d%H%M',time.localtime(time.time())))
# print(type(time.strftime('%Y%m%d%H%M',time.localtime(time.time()))))




# ## pingwest爬虫测试
# ptime = 1486993292
# url = 'http://www.pingwest.com/wp-admin/admin-ajax.php'
# data = {'action': 'my_recommand', 'secutity': 'b17e1ad3ea', 'postid': '', 'type': '1'}
# data['postid'] = ptime
#
# r = requests.post(url=url, data=data)
# html = r.content.decode('utf-8')
# # print(type(html),html)
# dicList = json.loads(html)
# print(dicList[0]['contenthtml'])
# inputFilePath = index.ROOT_PATH + '/data/pingwest_data/test.txt'
# fw = open(inputFilePath,'w',encoding='utf-8')
# fw.write(dicList[0]['contenthtml'])
# fw.close()



# # 测试读取36kr爬取内容
# filePath = index.ROOT_PATH + '/data/kr_data/' + 'origin_html.txt'
# fr = open(filePath,'r',encoding='utf-8')
# line = fr.readline()
# print(type(line),line)
# dic = json.loads(line)
# print(type(dic),dic)
# print(dic['data']['title'])
# print(dic['data']['published_at'])
# print(dic['data']['currentUrl'])
# print(type(dic['data']['extraction_tags']),dic['data']['extraction_tags'])
# originTag = json.loads(dic['data']['extraction_tags'])
# print(type(originTag),originTag,originTag[0],originTag[1][0])
# print(dic['data']['user']['name'])
# print(type(dic['data']['content']),dic['data']['content'])





# filePath = index.ROOT_PATH + '/data/pingwest_data/' + 'origin_html_pingwest_201701181122.txt'
# fr = open(filePath,'r',encoding='utf-8')
# line = fr.readline()
# print(type(line),line)
#
# dic = json.loads(line)
# print(type(dic),dic)
# print(type(dic[0]),dic[0])
# print(dic[0]['ptime'])





# postid = '1484687722'
# url = 'http://www.pingwest.com/wp-admin/admin-ajax.php'
# data = {'action': 'my_recommand', 'secutity': 'b17e1ad3ea', 'postid': '', 'type': '1'}
# data['postid'] = postid
#
# r = requests.post(url=url, data=data)
# html = r.content.decode('utf-8')
# # print(type(html),html)
# dic = json.loads(html)
# print(type(dic),dic)





# ## 36kr爬取的单元测试
# url = "http://36kr.com/api/post/5059724/next"
# header = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36' }
# r = requests.get(url=url,headers=header)
# html = r.content.decode('utf-8')
# # print(html)
# dic = json.loads(html)
# print(type(dic),dic)
# i = 1
# while dic['data']['id']:
#     url = "http://36kr.com/api/post/" + str(dic['data']['id']) + "/next"
#     r = requests.get(url=url, headers=header)
#     dic = json.loads(r.content.decode('utf-8'))
#     print(i,type(dic), dic)
#     i += 1



## 1 获取标签
# extraction_tags = dic['data']['extraction_tags']
# print(eval(extraction_tags))
# print(type(eval(extraction_tags)))

## 2 获取其他相关文章
# extra = dic['data']['extra']
# print(type(extra),extra)
# dic = json.loads(extra)
# print(type(dic),dic)



# for item in extraction_tags:
#     print(type(item[0]))
#     print(item[0])

# print(r.content)
# print(type(json.loads(r.content.decode())))

# r.encoding = 'utf-8'
# html = r.text
# print(type(html))
# print(html)
# dic = eval(html)
# print(type(dic))
# print(dic)

# html = r.content.decode()
# print(type(html))
# print(html)
# json = json.loads(html)
# print(json)



# test = [['\"\\u6c7d\\u8f66\"',1],['\"\\u7279\\u65af\\u62c9\"',2],['\"\\u65e0\\u4eba\\u9a7e\\u9a76\"',2]]
# for item in test:
#     print(item[0])





# testHtml = """<p><a href="http://thenextweb.com/apple/2013/07/26/apples-developer-center-returns-after-8-day-outage-due-to-security-breach/" target="_blank">1.\xa0苹果开发者中心重新上线</a></p>\n<p>在经历了8天的安全事故后，苹果开发者中心今天终于重新上线。目前开发者中心的主页面已经恢复，但其余的板块仍然处待恢复阶段，如论坛、技术支持和预发布文档等依然没有上线。</p>\n<p>苹果于上周四关闭开发者中心的部分功能，称遭遇外来入侵要进行全面检查。尽管苹果尽最大努力对开发者的账号进行维护，但仍有不少开发者报告称遇到了各种障碍。</p>\n<p><a href="http://www.pingwest.com/pw-7-27-13/apple-devcenter-730x296/" rel="attachment wp-att-19167"><img class="alignnone size-medium wp-image-19167" alt="apple-devcenter-730x296" src="http://cdn.pingwest.com/wp-content/uploads/2013/07/apple-devcenter-730x296-660x267.png?imageView2/2/w/750/q/90" width="660" height="267" /></a></p>\n<p>本周早些时候，苹果发布了一个开发者状态追踪工具，帮助开发者了解目前开发者中心各个板块的恢复情况。苹果称，开发者中心的服务会逐步恢复，先是证书、论坛和Bug报告等，再是软件下载。</p>\n<p><a href="http://thenextweb.com/google/2013/07/26/so-much-for-launch-dates-googles-new-nexus-7-tablet-has-landed-in-the-google-play-store/" target="_blank">2.\xa0新款Nexus 7现已在Play Store开卖</a></p>\n<p>Google刚刚发布的新款Nexus 7平板电脑目前已经在Play Store开卖，从今日起用户可以订购16G和32G两种型号的Nexus 7，售价229美元。据Play Store页面显示，产品订购后要等到7月30日才能出货。早在Nexus 7发布的前一天，BestBuy就提前开放了该设备的预定。</p>\n<p><a href="http://techcrunch.com/2013/07/26/google-asks-glass-developers-to-start-working-on-android-based-apps-ahead-of-glass-development-kit-launch/" target="_blank">3.\xa0Google鼓励开发者先开发Android版的Google Glass应用</a></p>\n<p>目前开发者在Google Glass上开发的应用仅限于一些基于网页的应用，因为API的权限十分有限。要想开发原生的Glass应用必须要等到Google的Glass Development Kit（GDK）发布。而今天Google<a href="https://plus.google.com/u/0/+GoogleDevelopers/posts/d2qgQgL7E2g" target="_blank">发文</a>称，开发者可以先用Android的SDK开发他们设想的Glass应用，这意味着GDK即将到来。</p>\n<p><a href="邮件管理应用Mailbox的开发团队日前宣布，其To-Do类事务管理应用Orchestra即将于9月6日关闭，并将把主要精力放在Mailbox的开发上。去年9月开发团队暂停Orchestra的开发工作转而开发Mailbox。该公司于今年3月份被Dropbox收购。" target="_blank">4.\xa0Mailbox开发团队即将关闭旗下Orchestra产品</a></p>\n<p>邮件管理应用Mailbox的开发团队日前宣布，其To-Do类事务管理应用Orchestra即将于9月6日关闭，并将把主要精力放在Mailbox的开发上。去年9月开发团队暂停Orchestra的开发工作转而开发Mailbox。该公司于今年3月份被Dropbox收购。</p>\n<p><a href="http://www.pcmag.com/article2/0,2817,2422295,00.asp" target="_blank">5.\xa0Google Translate现支持45种语言手写输入</a></p>\n<p>日前Google Translate添加了一项新的功能，手写输入。早在2012年1月，Google Translate的Android版应用就已经支持手写输入了，而此次Google把这一功能放到了网页版上。目前Google Translate支持45种语言的手写输入，包括汉语、日语和韩语。\n<p class="post-footer-wx"><img src="http://cdn.pingwest.com/wp-content/themes/pingwest201603/images/pw-wexin-qr.jpg"><span class="qr-des"><span>微信订阅 <b>PingWest 品玩</b></span><span>请关注公众号：wepingwest ，有品好玩的科技，更早一步看到。</span></span></p>\n<p><a href="http://www.pingwest.com/pw-7-25-2013/chromecast/" rel="attachment wp-att-19050"><img class="alignnone size-full wp-image-19050" alt="chromecast" src="http://cdn.pingwest.com/wp-content/uploads/2013/07/chromecast.png?imageView2/2/w/750/q/90" width="379" height="400" /></a></p>\n
# <p>【1】<a href="http://googleblog.blogspot.com/2013/07/from-tvs-to-tablets-everything-you-love.html">Google发布电视U盘，售价35美元</a></p>\n<p>今天凌晨，Google在旧金山举办的产品发布会上，发布了一款电视U盘产品——Chromecast，售价35美元，折合成人民币215元。</p>\n
# <p>Chromecast外型酷似U盘，可以与电视的HDMI接口相连。连接之后，将允许手机（包括Android、iOS）、平板以及电脑上的内容投射（cast）到电视上，支持的应用包括Netflix、YouTube、 Google Play Movies &amp; TV以及Google Play Music，并且Pandora等应用将在不久时间内支持这一功能。用户可以使用各种智能设备对电视进行操控，同时还可以进行多任务操作——在电视上看视频的同时也可以用手机发邮件。</p>\n<p>在Google看来，发布这款将电视和各种智能设备（手机、平板和电脑）连接起来的设备，是为了向用户提供一个简单的内容提供解决方案，也是Google希望更大程度参与家庭娱乐的举措。</p>\n
#
# <p>【2】<a href="http://allthingsd.com/20130724/facebook-beats-as-mobile-revenue-jumps-to-41-percent-of-ads-business/">Facebook发布第二季度财报</a></p>\n
# <p>今天，Facebook发布了截至6月30日的2013年第二季度财报。</p>\n<p>财报显示，Facebook第二季度营收为18.13亿美元，相较去年同期增长了53%；净利润为3.33亿美元，而去年同期为净亏损1.57亿美元。</p>\n
# <p>从财报来看，Facebook最亮眼的还是移动业务营收。第二季度，Facebook移动端广告营收占据总广告营收的41%，上一季度这一数据还是30%。</p>\n
# <p>【3】<a href="http://googleblog.blogspot.com/2013/07/from-tvs-to-tablets-everything-you-love.html">Google发布新版Nexus 7</a></p>\n
# <p>今天凌晨，Google发布了新版Nexus 7。</p>\n<p>新版Nexus 7采用的323 ppi的7寸屏，屏幕色彩表现相对之前版本提升了30%，配备120万像素的前置摄像头以及500万的后置摄像头，使用1.5GHz高通骁龙S4 PRO处理器，2GB RAM。并且支持超过9个小时的视频播放，10个小时的网页浏览。</p>\n
# <p>全新的Nexus 7将于7月30日上市，16G Wifi版本售价为229美元。</p>\n
# <p>【4】<a href="http://googleblog.blogspot.com/2013/07/from-tvs-to-tablets-everything-you-love.html">Android 4.3发布</a></p>\n
# <p>今天凌晨，Google正式发布了Android 4.3，Nexus 7将是第一款搭载Android 4.3的设备。</p>\n
# <p><a href="http://digi.tech.qq.com/a/20130725/000534.htm">相比Android 4.2, 4.3主要有以下变化：</a></p>\n
# <blockquote><p>1.支持多用户登录<br />\n2.Bluetooth Smart：实现蓝牙低功耗<br />\n3.支持OpenGL ES 3.0：将为Android游戏带来更出色的视觉体验<br />\n
# 4.DRM APIs：为一些在线视频软件提供了全新的数字版权加密技术支持</p></blockquote>\n
# <p>【5】<a href="http://9to5google.com/2013/07/24/google-hits-70m-tablet-activations-1m-apps-in-the-play-store/">Android平板达到7000万激活量</a></p>\n<p>在今天的发布会上，Android和Chrome主管Sundar Pichai宣布，Android平板的激活量达到7000万，而去年同期这一数据为1000万。</p>\n
# <p>同时，目前Google Play应用数超过100万，有500亿的App下载量。</p>\n
# <p>&nbsp;</p>\n<p>&nbsp;</p>\n<p>&nbsp;</p>\n<p>&nbsp;\n<p class="post-footer-wx"><img src="http://cdn.pingwest.com/wp-content/themes/pingwest201603/images/pw-wexin-qr.jpg"><span class="qr-des"><span>微信订阅 <b>PingWest 品玩</b></span><span>请关注公众号：wepingwest ，有品好玩的科技，更早一步看到。</span></span></p>\n
# <p><img class="alignnone size-full wp-image-7000" alt="G+d" src="http://cdn.pingwest.com/wp-content/uploads/2013/02/G+d5.jpg?imageView2/2/w/750/q/90" width="490" height="312" /></p>\n
# <p><strong>[1] 巨头决战前夕</strong></p>\n
# <p>上周六晚间，京东商城对外披露<a href="http://www.pingwest.com/360buy-kingdom/" target="_blank">完成7亿美元融资</a>，主要投资者加拿大安大略教师退休基金和沙特亿万富翁阿尔瓦利德王子控股的王国控股集团，都已不是普通的VC，王国控股更是把投资上升到<a href="http://tech.sina.com.cn/i/2013-02-17/11288064747.shtml" target="_blank">“巩固沙特与中国战略关系”</a>的层面。</p>\n
# <p>次日，它的主要竞争对手也都以不同渠道放出风来——<a href="http://tech.163.com/13/0217/09/8NTG48TK000915BD.html" target="_blank">阿里巴巴：投行报告阿里估值达660亿美元至1280亿美元之间</a>，若今年上市，市值可达800亿美元；<a href="http://tech.sina.com.cn/i/2013-02-18/03338065984.shtml" target="_blank">苏宁：张近东内部讲话披露</a>，称电子商务发展要由零售企业主导，并将对组织架构、年度计划、经营策略和人员任命全面进行部署。</p>\n
#
# <p><strong>[2] 唱空3D打印</strong></p>\n<p>过去两年频繁猎杀中国概念股的香橼<a href="http://finance.sina.com.cn/roll/20130218/011814565992.shtml" target="_blank">又瞄准了3D打印公司</a>，上周称“3D打印概念”公司估值过高，技术已被过分炒作。受其影响，3D打印概念股包括3DSystems、Stratasys和ExOne股价全面下跌。</p>\n
# <p>长期来看，市盈率高得离谱的3D打印公司确实需要业绩来支撑资本的信心，而行业生态中也确实需要这样的坏小子角色，提醒人们对过度热门的东西保持适度冷静。至于泡沫问题，我想提醒，奥巴马上周在国情咨文中公布了美国对3D打印的产业部署，中国近期也将公布3D打印的战略性规划和行业提振计划。</p>\n
#
# <p><strong>[3] 搜索引擎国家队</strong></p>\n<p>上周刚刚突破3000万微博粉丝的李开复，昨日疑因发微博质疑即刻搜索而遭禁言3天。</p>\n
# <p>依据相关政策，人民日报和新华社从两年多前开始组建搜索引擎“国家队”，人民日报交出的答案是即刻搜索，并聘请邓亚萍出任总经理。根据<a href="http://tech.sina.com.cn/i/2012-09-26/14277658902_2.shtml">南都周刊的报道</a>，邓亚萍到任后，在李开复的推荐下，邀请了谷歌中国工程院副院长刘骏出任首席科学家来重建技术。</p>\n
# <p>根据<a href="http://tech.sina.com.cn/i/2013-02-17/13488064884.shtml" target="_blank">新浪科技的报道</a>，即刻搜索是在刘骏的创业项目“云云搜索”的基础架构上搭建而成，早在去年第四季度，人民日报副总编辑、人民搜索董事长马利，对目前即刻搜索的现状并不满意。主要矛盾并非是投入过大，而是其未能完全掌握搜索的核心技术。</p>\n
#
# <p><strong>[4] 比特币</strong></p>\n
# <p>比特币诞生4年来，一直保持着不愠不火的状态，最近又连续成为报道主题，多家网站宣布支持比特币。</p>\n
# <p>云存储服务<a href="http://news.pingwest.com/archives/2558">Mega宣布支持比特币</a>，并公布了一系列付费选择。Kim Dotcom一直希望能尽可能不受政府监管，无法追踪的比特币支付是一种非常完美的方案。</p>\n
# <p>此外，热门的社交新闻网站<a href="http://it.sohu.com/20130217/n366269552.shtml">Reddit也宣布</a>接受比特币付款使用Gold服务，该服务提供一系列编辑工具，还可以为用户关闭广告。使用比特币也意味着其可以接受来自全球各地的付款。</p>\n
# <p>去年11月，博客平台Wordpress也宣布接受比特币，将该博客平台的部分付费功能向无法使用信用卡和PayPal支付的部分国家用户开放。</p>\n
#
# <p><strong>[5] Mozilla的使命</strong></p>\n
# <p>上周Opera浏览器宣布转向Chrome和Safari主导的WebKit内核。但<a href="http://news.pingwest.com/archives/2618">Mozilla还是发出了不一样的声音</a>，Mozilla首席技术官Brendan Eich在个人博客上表示，不要期待Firefox更换内核，作为一个非盈利项目，这款浏览器有着与其竞争对手不同的使命。我们不仅是一项业务，还有一个重要原因，就是Mozilla的存在能确保浏览器市场的多元化，因为垄断绝对不利于互联网的发展，这不仅是Mozilla坚守Gecko内核的一个理由，也是对IE浏览器的激励。</p>\n
# <p>我们欢迎多元化而带来的技术进步，反对出现下一个像当年的IE那样因为垄断而固步自封的悲剧。</p>\n
# <p>&nbsp;\n
# <p class="post-footer-wx"><img src="http://cdn.pingwest.com/wp-content/themes/pingwest201603/images/pw-wexin-qr.jpg"><span class="qr-des"><span>微信订阅 <b>PingWest 品玩</b></span><span>请关注公众号：wepingwest ，有品好玩的科技，更早一步看到。</span></span></p>\n """
#
#
#
#
#
# testHtml2 = """<p><strong>[1] 巨头决战前夕</strong></p>\n
# <p>上周六晚间，京东商城对外披露<a href="http://www.pingwest.com/360buy-kingdom/" target="_blank">完成7亿美元融资</a>，主要投资者加拿大安大略教师退休基金和沙特亿万富翁阿尔瓦利德王子控股的王国控股集团，都已不是普通的VC，王国控股更是把投资上升到<a href="http://tech.sina.com.cn/i/2013-02-17/11288064747.shtml" target="_blank">“巩固沙特与中国战略关系”</a>的层面。</p>\n
# <p>次日，它的主要竞争对手也都以不同渠道放出风来——<a href="http://tech.163.com/13/0217/09/8NTG48TK000915BD.html" target="_blank">阿里巴巴：投行报告阿里估值达660亿美元至1280亿美元之间</a>，若今年上市，市值可达800亿美元；<a href="http://tech.sina.com.cn/i/2013-02-18/03338065984.shtml" target="_blank">苏宁：张近东内部讲话披露</a>，称电子商务发展要由零售企业主导，并将对组织架构、年度计划、经营策略和人员任命全面进行部署。</p>\n
#
# <p><strong>[2] 唱空3D打印</strong></p>\n<p>过去两年频繁猎杀中国概念股的香橼<a href="http://finance.sina.com.cn/roll/20130218/011814565992.shtml" target="_blank">又瞄准了3D打印公司</a>，上周称“3D打印概念”公司估值过高，技术已被过分炒作。受其影响，3D打印概念股包括3DSystems、Stratasys和ExOne股价全面下跌。</p>\n
# <p>长期来看，市盈率高得离谱的3D打印公司确实需要业绩来支撑资本的信心，而行业生态中也确实需要这样的坏小子角色，提醒人们对过度热门的东西保持适度冷静。至于泡沫问题，我想提醒，奥巴马上周在国情咨文中公布了美国对3D打印的产业部署，中国近期也将公布3D打印的战略性规划和行业提振计划。</p>\n
#
# <p><strong>[3] 搜索引擎国家队</strong></p>\n<p>上周刚刚突破3000万微博粉丝的李开复，昨日疑因发微博质疑即刻搜索而遭禁言3天。</p>\n
# <p>依据相关政策，人民日报和新华社从两年多前开始组建搜索引擎“国家队”，人民日报交出的答案是即刻搜索，并聘请邓亚萍出任总经理。根据<a href="http://tech.sina.com.cn/i/2012-09-26/14277658902_2.shtml">南都周刊的报道</a>，邓亚萍到任后，在李开复的推荐下，邀请了谷歌中国工程院副院长刘骏出任首席科学家来重建技术。</p>\n
# <p>根据<a href="http://tech.sina.com.cn/i/2013-02-17/13488064884.shtml" target="_blank">新浪科技的报道</a>，即刻搜索是在刘骏的创业项目“云云搜索”的基础架构上搭建而成，早在去年第四季度，人民日报副总编辑、人民搜索董事长马利，对目前即刻搜索的现状并不满意。主要矛盾并非是投入过大，而是其未能完全掌握搜索的核心技术。</p>\n
#
# <p><strong>[4] 比特币</strong></p>\n
# <p>比特币诞生4年来，一直保持着不愠不火的状态，最近又连续成为报道主题，多家网站宣布支持比特币。</p>\n
# <p>云存储服务<a href="http://news.pingwest.com/archives/2558">Mega宣布支持比特币</a>，并公布了一系列付费选择。Kim Dotcom一直希望能尽可能不受政府监管，无法追踪的比特币支付是一种非常完美的方案。</p>\n
# <p>此外，热门的社交新闻网站<a href="http://it.sohu.com/20130217/n366269552.shtml">Reddit也宣布</a>接受比特币付款使用Gold服务，该服务提供一系列编辑工具，还可以为用户关闭广告。使用比特币也意味着其可以接受来自全球各地的付款。</p>\n
# <p>去年11月，博客平台Wordpress也宣布接受比特币，将该博客平台的部分付费功能向无法使用信用卡和PayPal支付的部分国家用户开放。</p>\n
#
# <p><strong>[5] Mozilla的使命</strong></p>\n
# <p>上周Opera浏览器宣布转向Chrome和Safari主导的WebKit内核。但<a href="http://news.pingwest.com/archives/2618">Mozilla还是发出了不一样的声音</a>，Mozilla首席技术官Brendan Eich在个人博客上表示，不要期待Firefox更换内核，作为一个非盈利项目，这款浏览器有着与其竞争对手不同的使命。我们不仅是一项业务，还有一个重要原因，就是Mozilla的存在能确保浏览器市场的多元化，因为垄断绝对不利于互联网的发展，这不仅是Mozilla坚守Gecko内核的一个理由，也是对IE浏览器的激励。</p>\n
# <p>我们欢迎多元化而带来的技术进步，反对出现下一个像当年的IE那样因为垄断而固步自封的悲剧。</p>\n
# <p>&nbsp;\n
# <p class="post-footer-wx"><img src="http://cdn.pingwest.com/wp-content/themes/pingwest201603/images/pw-wexin-qr.jpg"><span class="qr-des"><span>微信订阅 <b>PingWest 品玩</b></span><span>请关注公众号：wepingwest ，有品好玩的科技，更早一步看到。</span></span></p>\n  """
#
# resultList = testHtml2.split('\n')
# # print(len(resultList))
# # pattern1 = re.compsile('>[0-9][.):：、,，]',re.S)
# # pattern1 = re.compile('>[0-9][.):：、,，][\u4E00-\u9FA5|a-zA-Z]',re.S)
# # pattern2 = re.compile('>[【|\[][0-9][\]|】]',re.S)
# pattern3 = re.compile('(>[0-9][.):：、,，])|(>[【|\[][0-9][\]|】])',re.S)
# articleList = []
# boatList = []
# finalArticleList = []
# for item in resultList:
#     if pattern3.findall(item):
#         # print(pattern3.findall(item),item)
#         # print(pattern3.findall(item)[0])
#         if boatList:
#             articleList.append(boatList)
#             boatList = []
#         boatList.append(item)
#     else:
#         boatList.append(item)
# # print(len(articleList))
# for item in articleList:
#     print(item)
#     if item[0]:
#         title = getTitle(item[0])
#     contentList = item[1:]
#     content = getContent(''.join(contentList))
#     finalArticleList.append([title,content])





# patn1 = re.compile('[。|？|！|”][0-9][.|)|）|：|:|、|,|，]', re.S)
# patn2 = re.compile('[。|？|！|”]【[0-9]】', re.S)
# patn3 = re.compile('[。|？|！|”]\[[0-9]\]', re.S)



# print(1303-1281)
# print(22/10530)
# test = '哈哈'
# result = test.split(' ')
# print(result)



# test = """<p>对于一款要日常佩戴的智能眼镜来说，外形没有大亮点可能才是真正的亮点。</p>\n<p>最近，Kickstarter上爆出一匹黑马。短短的几天之内，一款<a href="https://www.kickstarter.com/projects/vue/vue-your-everyday-smart-glasses?ref=ahnvz8">智能眼镜</a>就众筹到190万美金，约合1300万人民币。跟它上线前仅5万美金的众筹目标，翻了近40倍。</p>\n<p>包括Business Insider、TechCrunch、Forbes （福布斯）在内的一些美国媒体对它的评价都是：超越Google Glass，成为人们生活中真正需要的一款智能眼镜。</p>\n<p>这款骨传导智能眼镜除了有各种先进技术和实用功能外，它最大的特点就是它长得和你平日里戴的眼镜一毛一样——不会让你成为街头上众人眼中的异类，而这本该是一款智能眼镜最基本的要素，却往往被大家所忽视。</p>\n<p>外界曾经对于Google Glass最大的评价就是外表看起来太过于极客了，让人看起来很奇怪。而其他设备也一样会让使用者看起来很奇怪，并不适合天天走在街上随时佩戴。</p>\n<p><img class=" wp-image-95757 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/vue1.gif?imageView2/2/w/750/q/90" alt="vue1" width="562" height="316" /></p>\n<p>说不定当你用Google眼镜锁定别人的时候，别人会觉得嗯，这个疯子&#8230;&#8230;.</p>\n<p><img class=" wp-image-95758 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/vue2.gif?imageView2/2/w/750/q/90" alt="vue2" width="482" height="271" /></p>\n<p>不过，这款名字被命名为<a href="https://www.kickstarter.com/projects/vue/vue-your-everyday-smart-glasses?ref=ahnvz8">Vue</a>的眼镜却彻底颠覆了智能眼镜外观的诟病，而是采取了和一般眼镜一样的外观。这款产品分为两个版本：经典款以及流行款。针对用户个人需要，镜片也可以更换为近视镜片，没有度数的镜片以及墨镜。</p>\n<p><img class=" wp-image-95768 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/Screen-Shot-2016-12-08-at-2.23.12-AM.png?imageView2/2/w/750/q/90" alt="Screen Shot 2016-12-08 at 2.23.12 AM" width="526" height="290" /></p>\n<p>从外观上看，完全看不出它和一般眼镜有什么太大的区别。但是，这这这&#8230;..怎么让别人知道我戴的是这么牛的眼镜呢？？</p>\n<p>别着急，只要随便在眼镜腿儿上点点点就可以昭告世界你的眼镜有多神奇啦。</p>\n<h2>通话</h2>\n<p>用户接听电话的时候，只需要点点眼镜腿就可以接听电话了。</p>\n<p><img class=" wp-image-95759 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/vue3.gif?imageView2/2/w/750/q/90" alt="vue3" width="523" height="294" /></p>\n<p>利用骨传导技术，手机的声波直接通过对骨头的振动传至听神经。跟Google Glass的单边骨传导相比较，这款眼镜采用的是双耳骨传导。这样接电话除了不用掏出手机非常方便外，也非常有利于保护自己的隐私。这种通过振动传播的声音是只有本人能够听到的，外人是完全听不到的。而同时眼镜中的内置话筒会进行收音，没有了恼人的耳机和绕绕绕绕绕绕绕不明白的耳机线是不是清爽非常多？</p>\n<p><img class="size-full wp-image-95767 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/Screen-Shot-2016-12-08-at-2.13.42-AM.png?imageView2/2/w/750/q/90" alt="Screen Shot 2016-12-08 at 2.13.42 AM" width="471" height="258" /></p>\n<h2>拍照</h2>\n<p>除了简单的接听电话功能，这款耳机还是个可以随时随地带在身边的摄像师哦。摆好你的手机，点击一下眼镜就可以遥控手机给自己自拍了。这可比自拍杆酷太多了。</p>\n<p><img class=" wp-image-95760 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/vue4.gif?imageView2/2/w/750/q/90" alt="vue4" width="510" height="287" /></p>\n<h2>导航</h2>\n<p>不过，作为一个不折不扣的路痴，我个人最喜欢的还是这款眼镜的导航功能——可以随时在你开车走路时提醒你下一步该去向哪里。除此外，它还有通过触控来控制音乐播放的功能。</p>\n<p><img class=" wp-image-95807 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/vue11.gif?imageView2/2/w/750/q/90" alt="vue11" width="576" height="324" /></p>\n<h2>健康</h2>\n<p>运动时，这款眼镜可以取代运动手环，为你记录并随时报告你的运动状况，例如所消耗的卡路里以及心率等等有效信息。</p>\n<p>除此以外，当佩戴它的用户忙于工作久坐的时候，它还会贴心地提醒你站起来活动活动。<br />\n<img class=" wp-image-95806 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/vue10.gif?imageView2/2/w/750/q/90" alt="vue10" width="597" height="336" /></p>\n<h2>无线充电及超长待机</h2>\n<p>这样酷的一款耳机也有着非常特殊的充电方式。只需要将眼镜放回眼镜盒就可以无线充电。一次充电可以使用超过1周的时间。<br />\n<img class=" wp-image-95770 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/Screen-Shot-2016-12-08-at-2.23.41-AM.png?imageView2/2/w/750/q/90" alt="Screen Shot 2016-12-08 at 2.23.41 AM" width="595" height="321" /></p>\n<p>此外，那些不经意间总是丢三落四的用户也终于被拯救。这款智能眼镜的搜索定位功能可以让你轻松让你找到眼镜。再也不用担心早上出门之前因为丢三落四而被迟到了。</p>\n<p><img class=" wp-image-95762 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/vue7.gif?imageView2/2/w/750/q/90" alt="vue7" width="612" height="344" /></p>\n<p>这款眼镜在<a href="https://www.kickstarter.com/projects/vue/vue-your-everyday-smart-glasses?ref=ahnvz8">Kickstarter</a>目前的售价是179美金，且众筹将于本周结束，其预定发货时间为2017年7月。截止到现在，这款产品已经在Kickstarter上众筹超过190万美金，约合1300万人民币。</p>\n<p>研发这款产品背后的创业公司Vigo Technology Inc.有着一半的中国血统，创始人桂家勋、张甜甜均为美国宾夕法尼亚大学毕业。这家公司目前在美国旧金山和中国深圳都有分部。</p>\n<p><img class="size-full wp-image-95812 aligncenter" src="http://cdn.pingwest.com/wp-content/uploads/2016/12/Screen-Shot-2016-12-08-at-3.02.28-PM.png?imageView2/2/w/750/q/90" alt="Screen Shot 2016-12-08 at 3.02.28 PM" width="640" height="213" /></p>\n<p>最后，让我们看一下这款产品的介绍视频：</p>\n<p><iframe src="http://player.youku.com/embed/XMTg1NTg1NTA5Ng==" width="510" height="498" frameborder="0" allowfullscreen="allowfullscreen"></iframe>\n<p class="post-footer-wx"><img src="http://cdn.pingwest.com/wp-content/themes/pingwest201603/images/pw-wexin-qr.jpg"><span class="qr-des"><span>微信订阅 <b>PingWest 品玩</b></span><span>请关注公众号：wepingwest ，有品好玩的科技，更早一步看到。</span></span></p>\n
# """
# result = crawl.extractContentFromHtmlString(test)
# for item in result:
#     print(item)


# url = 'https://www.huxiu.com/v2_action/article_list'
# # data = {'huxiu_hash_code':'682dcdbec88b3e50e6b83ad7ac598724','page':'4','last_dateline':'1481263920'}
# data = {'page':'4'}
# header = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36' }
# r = requests.post(url=url,data=data,headers=header)
# print(type(r.text))
# print(r.text)
# dicList = json.loads(r.text)
# print(dicList['data'])
#
# data = {'page':'5'}
# header = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36' }
# r = requests.post(url=url,data=data,headers=header)
# print(type(r.text))
# print(r.text)
# dicList = json.loads(r.text)
# print(dicList['data'])







# # md5解密：
# """
# huxiu_hash_code	682dcdbec88b3e50e6b83ad7ac598724
# page	4
# last_dateline	1481263920
# """
# test = '1481263920'
# print(hashlib.md5(test.encode('utf-8')).hexdigest())






# fw = open('testtext.txt','w',encoding='utf-8')
#
# i = 1
#
# url = 'http://www.pingwest.com/wp-admin/admin-ajax.php'
# data = {'action':'my_recommand','secutity':'b17e1ad3ea','postid':'1481532552','type':'1'}
# r = requests.post(url=url,data=data)
# print(r.text)
# print(type(r.text))
# print(r.text[0])
# dicList = json.loads(r.text)
# print(dicList)
# print(type(dicList[0]))
# print(dicList[0]['title'],dicList[0]['ptime'])
# # fw.write(str(dic[0]['contenthtml']).replace('\n','').replace('\r','').replace('\t','') + '\n')
# # content = str(dicList[0]).replace('\n','').replace('\r','').replace('\t','')
# content = str(dicList[0])
# fw.write(content)
# fw.close()
# try:
#     while dic[0]['ptime']:
#         postid = dic[0]['ptime']
#         data['postid'] = postid
#         r = requests.post(url=url,data=data)
#         dic = json.loads(r.text)
#         i += 1
#         print(i,dic[0]['title'],dic[0]['ptime'])
#         fw.write(str(dic[0]['contenthtml']).replace('\n', '').replace('\r', '').replace('\t', '') + '\n')
#     fw.close()
# except Exception as ex:
#     fw.close()




# # 對存儲的數據處理測試
# fr = open('testtext.txt','r',encoding='utf-8')
# line = fr.readline().replace('\n','')
# print(type(line))
# print(line)
# result = eval(line)
# print(type(result))











# data = {'action':'my_recommand','secutity':'b17e1ad3ea','postid':'1481199510','type':'1'}
# r = requests.post(url=url,data=data)
# dic = json.loads(r.text)
# print(dic[0]['title'])
# print(dic[0]['ptime'])
# data = {'action':'my_recommand','secutity':'b17e1ad3ea','postid':'1481172058','type':'1'}
# r = requests.post(url=url,data=data)
# dic = json.loads(r.text)
# print(dic[0]['title'])
# print(dic[0]['ptime'])
# data = {'action':'my_recommand','secutity':'b17e1ad3ea','postid':'1481150572','type':'1'}
# r = requests.post(url=url,data=data)
# dic = json.loads(r.text)
# print(dic[0]['title'])
# print(dic[0]['ptime'])
# print(dic[0]['contenthtml'])
# print(dic[0]['title'])


# test = "\u60f3\u5b66papi\u9171\u7684\u4eba\u592a\u591a\uff0c\u77ed\u89c6\u9891\u57f9\u8bad\u8981\u706b\uff1f"
# print(test.encode('utf-8').decode('utf-8'))
# print(test)


# test = 'jsjaJ是jfk'
# test2 = "'"+ test +"'"


# param = {'p':2}
# url = 'http://www.jiemodui.com/Api/Index/news'
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
# r = requests.get(url=url,params=param,headers=headers)
# print(r.encoding)
# content = r.text
# print(content)
# dic = json.loads(content)
#
#
# print(dic)
# print(dic['list'][0]['name'])
# print(r.text)
# print(r.url)
# print(r.headers)
# print(r.request.headers)
# r.json()
# r.encoding = 'utf-8'
# print(r.encoding)
# print(r.content)
# print(chardet.detect(r.text))
# result = r.text.encode('utf8')
# print(result)
# print(chardet.detect(result))




# testStr = 'jjkas就看撒'    # 这个testStr变量是unicode编码，被称作 str
# result1 = testStr.encode('gbk')
# result2 = testStr.encode('utf-8')
# print(chardet.detect(result1))
# print(chardet.detect(result2))






# handle.mergeExcelFromFixedDirNewseed([],'')



# testList = []
# reList = [[1],[2],[3]]
# # testList.append(reList)     # [[[1], [2], [3]]]
# testList.extend(reList)
# print(testList)



# filePath = os.path.join(os.path.dirname(__file__),'data','newseed_data','resultSet','test.xls')
# r_xls = xlrd.open_workbook(filePath)
# r_sheet = r_xls.sheet_by_index(0)
# rows = r_sheet.nrows
# # result = r_sheet.row_values(0)
# # print(type(result))
# # print(result)
# for i in range(rows):
#     print(r_sheet.row_values(i))





# testStr = '2010年09月01日成立'
# testStr2 = '2007年09月成立'
#
# result = re.findall('([0-9]+)',testStr2,re.S)
# print(result)



# html = """<p>
# 2012年10月09日成立
# <i class="slash">/</i>
# 北京市
# </p>"""
# reList = crawl.extractContentFromHtmlString(html)
# print(reList)



# pageLinkList = ['http://newseed.pedaily.cn/vc/p1','http://newseed.pedaily.cn/vc/p2']
#
# result = linkList.getCompanyLinkIndexList(pageLinkList)
# print(result)


# # 使用python判断文件是否存在
# filePath1 = os.path.join(os.path.dirname(__file__),'data','newseed_data','investEvent_linkIndex_test.txt')
# filePath2 = os.path.join(os.path.dirname(__file__),'data','test.txt')
# if os.path.exists(filePath1):
#     print(filePath1,'1存在')
# if os.path.exists(filePath2):
#     print(filePath2,'2存在')



# html = """<p>
# <p class="keyword">
# <span class="btn red">企</span>
# <a class="btn default" href="/company/43614" target="_blank">乐视汽车(LeSEE乐视超级汽车)</a>
# <span class="btn blue">投</span>
# <a class="default" href="/vc/36904" target="_blank">深创投</a>
# <a class="default" href="/vc/31890" target="_blank">联想控股</a>
# <a class="default" href="/vc/39299" target="_blank">英大资本</a>
# <span id="#" class="default">民生信托</span>
# <a class="default" href="/vc/31186" target="_blank">华夏润石（新华联集团）</a>
# <span id="#" class="default">宏兆基金</span>
# </p>"""
# investCompanyStr = re.search('投</span>\s*(.*?)\s*</p>',str(html),re.S).group(1)
# investCompanySoup = BeautifulSoup(investCompanyStr)
# resultSetSpantag = investCompanySoup.find_all('span')
# if resultSetSpantag:
#     for spanTag in resultSetSpantag:
#         print(str(spanTag))
#         content = crawl.getStringBySpantag(str(spanTag))
#         print(content)




#
# html = """<span class="btn blue">投</span>
# <a class="default" href="/vc/35782" target="_blank">光信资本</a>
# <a class="default" href="/vc/24573" target="_blank">源码资本</a>
# <a class="default" href="/vc/31886" target="_blank">洪泰基金</a>
# <a class="default" href="/vc/8572" target="_blank">创新工场</a>
# <a class="default" href="/vc/533" target="_blank">晨兴创投</a>
# <span id="#" class="default">51信用卡</span>
# </p>"""
#
# investCompanyStr = re.search('投</span>\s*(.*?)\s*</p>',html,re.S).group(1)
# # print(investCompanyStr)
#
# investSoup = BeautifulSoup(investCompanyStr)
# resultA = investSoup.find_all('a')
# print(type(resultA))
# for item in resultA:
#     print(item)
#     print(str(item))
#     print(type(item))
# print(type(result))
# print(result)


# result = re.findall('target="_blank">\s*(.*?)\s*</a>',investCompanyStr,re.S)
# relink = re.findall('class="default" href="(.*?)" target="',investCompanyStr,re.S)
# print(result)
# print(relink)





# infoList = [('妙品','/invest/444'),('大大','/vc/456')]
# name,link = linkList.getCompanyNameAndLinkStr(infoList)
# print(name)
# print(link)




# infoList = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# infoList2 = [[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]]
# # outputFilePath = 'D:\\workstation\\repositories\\netspider\\data\\newseed_data\\result\\test.xls'
# outputFilePath = os.path.join(os.path.dirname(__file__),'data','newseed_data','resultSet','test.xls')
# # io.writeContent2Excel(infoList,outputFilePath)
# # io.appendContent2Excel(infoList2,outputFilePath)
# io.appendContent2Excel_test(infoList,outputFilePath)



# companyName = 'company'
# # companyName = companyName[0:len(companyName) - 1]
# # print(companyName)
# print(companyName[0:1])





# string = """技术的咖啡机啊看<jdskaf>健康收到了就啊大家"""
# print(string)
# result = re.sub('<.*?>','',string)
# print(result)




# newTimeStr = '2016-09-25-15-00'
# structTime = time.strptime(newTimeStr, '%Y-%m-%d-%H-%M')
# timeStamp = int(time.mktime(structTime))
# print(timeStamp)



# filePath = os.path.join(os.path.dirname(__file__),'test.xls')
# wb = Workbook()
# sheet = wb.active
# sheet.append(['Title','Time','Type','Money','productCompany','productCompanyLink','investCompany','investCompanyLink','investIntroduce'])
# wb.save(filePath)


# testList = ['','']
# if testList:
#     print('lll')



# string = """
# <p></p>
# <p>深圳市银桦投资管理有限公司投资雷士光电科技有限公司。</p>
# <p></p>"""
# singleContentList = []
# cleanedContentList = []
# contentList = crawl.extractContentFromHtmlString(string)
# print(contentList)
#
# for item in contentList:
#     if item :
#         singleContentList.append(item)
# print(singleContentList)
#
# for item in singleContentList:
#     temp = item.replace('\s','').replace('\t','').replace('\r','')
#     cleanedContentList.append(temp)
# print(cleanedContentList  )


# string = """<p> TMT </p>
# <p class="keyword">
# <span class="btn red">企</span>
# <a class="btn default" href="/company/2746" target="_blank">雷士光电科技有限公司 </a>
# <span class="btn blue">投</span>
# <a class="default" href="/vc/22210" target="_blank">银桦投资</a>
# </p>
# <p></p>
# <p>深圳市银桦投资管理有限公司投资雷士光电科技有限公司。</p>
# <p></p>"""
# # print(re.findall('keyword">\s*.*?\s*</p>\s*(.*?)\s*$',string,re.S))     #['<p></p>\n<p>深圳市银桦投资管理有限公司投资雷士光电科技有限公司。</p>\n<p></p>']
# print(re.findall('keyword">\s*.*?\s*</p>\s*(.*?)\s*',string,re.S))      #['']


# print(type('sss'))
# if type('sss') == str:
#     print('类型为字符串...')


# html = """<div class="info">
# <p>
# 2016年08月03日
# <i class="slash">/</i>
# 并购
# <i class="slash">/</i>
# 1000万人民币
# <i class="slash">/</i>
# 传统互联网
# </p>
# <p class="keyword">
# <span class="btn red">企</span>"""
# # result = re.search('info">\s*(.*?)\s*<p class="keyword">',str(html),re.S).group(1)
# # print(result)
# # crawl.extractContentFromHtmlString(result)
# html = BeautifulSoup(html)
# print(linkList.getTimeTypeAndMoney(html))


# html = """<div class="title">
# 邮件工具服务Front 获得 Social Capital 领投的1000 万美元 A 轮融资
# <a class="btn font-blue favor-add" data-resid="35391" data-restypeid="6" href="javascript:void(0);">"""
# result = re.search('title">\s*(.*?)\s*<a',str(html),re.S).group(1)
# print(result)



# # 目前来讲一个可行的读取文件的方式
# filePath = 'D:/workstation/repositories/netspider/data/newseed_data/acquisitionEvent_linkIndex_new.txt'
# try:
#     fr = open(filePath, 'r', encoding='utf-8')
#     i = 1
#     while True:
#         line = fr.readline().strip()
#         if line:
#             print(str(i),line)
#             i += 1
#         else:
#             break
#     fr.close()
# except Exception as err:
#     print('文件读取错误：',err)


# handle.listWrite2Txt(['1'],'/ddd','a.txt')


# url = 'http://newseed.pedaily.cn/invest/r225-p2'
# hooshSoup = crawl.getHooshSoup(url)
# tbodySoup = hooshSoup.find('tbody')
# print(tbodySoup)


# list = ['http://newseed.pedaily.cn/invest/r115-p1']
# linkList.getEventLinkIndexList(list)
# re = crawl.getHooshSoup('http://newseed.pedaily.cn/invest/r115-p1')
# print(re)


# initUrl = 'http://newseed.pedaily.cn/invest/r115-p1'
# print(str.replace(initUrl,initUrl[-1],'xxx'))


# print(handle.getPageLinkIndexList(170))

# print(math.ceil(173/10))