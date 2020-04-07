"""创建请求头池，IP池
在settings中DOWNLOADER_MIDDLEWARES开启中间件"""

import random
import time

class UserAgentDownloadMiddleware(object):
    user_agents=[ 'Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;AcooBrowser1.98.744;.NETCLR3.5.30729)',
        'Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;AcooBrowser1.98.744;.NETCLR3.5.30729)',
        'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;AcooBrowser;GTB5;Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1);InfoPath.1;.NETCLR3.5.30729;.NETCLR3.0.30618)',
        'Mozilla/4.0(compatible;MSIE8.0;WindowsNT5.1;Trident/4.0;SV1;AcooBrowser;.NETCLR2.0.50727;.NETCLR3.0.4506.2152;.NETCLR3.5.30729;AvantBrowser)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;AcooBrowser;SLCC1;.NETCLR2.0.50727;MediaCenterPC5.0;.NETCLR3.0.04506)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;AcooBrowser;GTB5;Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1);Maxthon;InfoPath.1;.NETCLR3.5.30729;.NETCLR3.0.30618)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;AcooBrowser;GTB5;',
        'Mozilla/4.0(compatible;Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;AcooBrowser1.98.744;.NETCLR3.5.30729);WindowsNT5.1;Trident/4.0)',
        'Mozilla/4.0(compatible;Mozilla/4.0(compatible;MSIE8.0;WindowsNT5.1;Trident/4.0;GTB6;AcooBrowser;.NETCLR1.1.4322;.NETCLR2.0.50727);WindowsNT5.1;Trident/4.0;Maxthon;.NETCLR2.0.50727;.NETCLR1.1.4322;InfoPath.2)',
        'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;AcooBrowser;GTB6;Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1);InfoPath.1;.NETCLR3.5.30729;.NETCLR3.0.30618)',
        'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;AcooBrowser;GTB5;Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1);InfoPath.1;.NETCLR3.5.30729;.NETCLR3.0.30618)',
        'Mozilla/4.0(compatible;MSIE8.0;WindowsNT5.1;Trident/4.0;GTB6;AcooBrowser;.NETCLR1.1.4322;.NETCLR2.0.50727)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;Trident/4.0;AcooBrowser;GTB5;Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1);InfoPath.1;.NETCLR3.5.30729;.NETCLR3.0.30618)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;AcooBrowser;SLCC1;.NETCLR2.0.50727;MediaCenterPC5.0;.NETCLR3.0.04506)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;AcooBrowser;GTB5;SLCC1;.NETCLR2.0.50727;MediaCenterPC5.0;.NETCLR3.0.04506)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;AcooBrowser;GTB5;Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1);InfoPath.1;.NETCLR3.5.30729;.NETCLR3.0.30618)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AcooBrowser;InfoPath.2;.NETCLR2.0.50727;AlexaToolbar)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AcooBrowser;.NETCLR2.0.50727;.NETCLR1.1.4322)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AcooBrowser;.NETCLR1.0.3705;.NETCLR1.1.4322;.NETCLR2.0.50727;FDM;.NETCLR3.0.04506.30;.NETCLR3.0.04506.648;.NETCLR3.5.21022;InfoPath.2)',
        'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;AcooBrowser;.NETCLR1.1.4322;.NETCLR2.0.50727)',
        'Mozilla/4.0(compatible;MSIE7.0;AmericaOnlineBrowser1.1;WindowsNT5.1;(R11.5);.NETCLR2.0.50727;InfoPath.1)',
        'Mozilla/4.0(compatible;MSIE7.0;AmericaOnlineBrowser1.1;rev1.5;WindowsNT5.1;.NETCLR1.1.4322;.NETCLR2.0.50727)',
        'Mozilla/4.0(compatible;MSIE7.0;AmericaOnlineBrowser1.1;rev1.5;WindowsNT5.1;.NETCLR1.1.4322)',
        'Mozilla/4.0(compatible;MSIE7.0;AmericaOnlineBrowser1.1;rev1.5;WindowsNT5.1;.NETCLR1.0.3705;.NETCLR1.1.4322;MediaCenterPC4.0;InfoPath.1;.NETCLR2.0.50727;MediaCenterPC3.0;InfoPath.2)',
        'Mozilla/4.0(compatible;MSIE7.0;AmericaOnlineBrowser1.1;rev1.2;WindowsNT5.1;SV1;.NETCLR1.1.4322)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;SV1;HbTools4.7.0)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;SV1;FunWebProducts;.NETCLR1.1.4322;InfoPath.1;HbTools4.8.0)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;SV1;FunWebProducts;.NETCLR1.0.3705;.NETCLR1.1.4322;MediaCenterPC3.1)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;SV1;.NETCLR1.1.4322;HbTools4.7.1)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;SV1;.NETCLR1.1.4322)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;SV1;.NETCLR1.0.3705;.NETCLR1.1.4322;MediaCenterPC3.1)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;SV1;.NETCLR1.0.3705;.NETCLR1.1.4322)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;SV1)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;FunWebProducts;(R11.5);HbTools4.7.7)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1;FunWebProducts)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.1)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;WindowsNT5.0)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;Windows98)',
        'Mozilla/4.0(compatible;MSIE6.0;AmericaOnlineBrowser1.1;rev1.5;WindowsNT5.1;SV1;FunWebProducts;.NETCLR1.1.4322)']
    def process_request(self,request,spider):
        user_agent=random.choice(self.user_agents)
        request.headers['User-Agent']=user_agent

class IPDownloadMiddleware(object):
    proxies=['http://ip:port']
    def process_request(self,request,spider):
        ip=random.choice(self.proxies)
        request.meta['proxy']=ip

#使用selenium下载，可在DOWNLOADER_MIDDLEWARES中开启该插件
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
    def process_request(self,request,spider):
        self.driver.get(request.url)
        time.sleep(3)
        source=self.driver.page_source
        response=HtmlResponse(url=self.driver.current_url,body=source,request=request,encoding='utf-8')
        return response

