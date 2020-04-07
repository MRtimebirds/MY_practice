#python3.5.3
#encoding='utf-8'

爬取中国机械社区（http://www.cmiw.cn/portal.php）首页页面中的社区交流下的8个版块：
'新科技/新产品', '汽车制造', '要闻热点', '技术研讨', '行业分析', '机器人', '能源储能', '人才就业'

爬取每篇文章的标题，所属版块，发布者，发布时间，浏览量，文章内容


保存方式：我在pipelines中写了几种方法：
1，直接保存在json中
2，保存在MongoDB
3，保存在MySQL中 #需要自己创建数据库，创建表，可用navicat可视化工具创建
4，MySQL的异步下载



中间件：
写了3种方法：
请求头池，IP池，scrapy中使用selenium打开网页获取源代码
#在settings中自己选择要使用的方法



增量爬取：
首先电脑里已经安装了redis数据库  #用于保存爬取过的url，用于实现去重
在settings中设置两行：
SCHEDULER='scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS='scrapy_redis.dupefilter.RFPDupeFilter'


最后说明一下，该爬虫只是个人的练习项目，代码可能还有很多需要优化的地方，
大佬们勿喷，有问题请大佬指出，感谢您的理解！

仅供学习参考，勿做非法使用，本人不负任何责任。