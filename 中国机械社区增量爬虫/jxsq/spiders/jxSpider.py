"""
python3.5.3
encoding='utf-8'
scrapy_redis增量爬取
爬取中国机械社区的‘社区交流’板块下8个版块：
'新科技/新产品', '汽车制造', '要闻热点', '技术研讨', '行业分析', '机器人', '能源储能', '人才就业'"""

import scrapy
from jxsq.items import JxsqItem
class JxspiderSpider(scrapy.Spider):
    name='jxSpider'
    allow_domains=['cmiw.cn']
    start_urls=['http://www.cmiw.cn/portal.php']

    def parse(self,response):
        #提取出【'新科技/新产品', '汽车制造', '要闻热点', '技术研讨', '行业分析', '机器人', '能源储能', '人才就业'】和对应的url
        classification_url=response.xpath('//div[@id="framejOoCzm"]//div[@class="block move-span"]/div/span[@class="titletext"]/a/@href').getall()
        classification=response.xpath('//div[@id="framejOoCzm"]//div[@class="block move-span"]/div/span[@class="titletext"]/a/text()').getall()
        for i in range(len(classification)):
            #对8个板块发起请求，classification使用meta传递给parse_item
            yield scrapy.Request(classification_url[i],callback=self.parse_item,meta={'info':(classification[i])})

    def parse_item(self,response):
        classification=response.meta.get('info')
        #提取页面中的文章标题和链接
        bm=response.xpath('//div[@class="bm_c xld"]//dl[@class="bbda cl"]')
        for dl in bm:
            title=dl.xpath('.//dt[@class="xs2"]/a/text()').get()
            title_url=dl.xpath('.//dt[@class="xs2"]/a/@href').get()
            # print(title)
            #访问文章页面
            yield scrapy.Request(title_url,callback=self.parse_detail,meta={'info':(title,classification)})
        try:
            next_page=response.xpath('//a[@class="nxt"]/@href').get()
            yield scrapy.Request(next_page,callback=self.parse)
        except:
            print('该版块已经爬取完了')

    def parse_detail(self,response):
        title,classification = response.meta.get('info')
        print('标题:',title)
        publisher=response.xpath('//p[@class="xg1"]//a/text()').get()
        print('发布者：',publisher)
        times=response.xpath('//p[@class="xg1"]/text()').get().strip()
        print(times)
        viewnum=response.xpath('//p[@class="xg1"]//em[@id="_viewnum"]/text()').get()
        print('阅读量：',viewnum,'人')
        article=''.join(response.xpath('//td[@id="article_content"]//text()').getall())
        # print(article)
        item=JxsqItem(classification=classification,title=title,publisher=publisher,times=times,viewnum=viewnum,article=article)
        yield  item





