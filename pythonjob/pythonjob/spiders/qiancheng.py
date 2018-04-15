# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class QianchengSpider(CrawlSpider):
    name = 'qiancheng'
    allowed_domains = ['51job.com']
    start_urls = ["https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html"]

    def parse(self,response):  #此response为每一页的响应
        #获取每一页的工作详情链接
        links = response.xpath('.//div[@class="el"]/p/span/a/@href').extract()
        for link in links:
            yield scrapy.Request(link,callback=self.parse_job)

        #获取下一页的链接
        i = 2
        while i <=722:
            next_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,"+str(i)+".html"
            i = i+1
            yield scrapy.Request(next_url,callback=self.parse)
        print (response.url)

        '''
        #获取下一页的链接  此方法有问题
        next_url = response.xpath('.//a[contains(text(),"下一页")]/@href').extract_first()
        #将下一页的链接丢给parse函数处理，继续得到工作详情链接和下一页链接
        yield scrapy.Request(next_url,callback=self.parse)             
        print (response.url)
        '''
        

    #定义处理工作详情页面的函数 parse_job
    def parse_job(self, response):   #此处的response为工作详情页面的响应内容
        #print ("----------------Start------------------") 
        print (response.url)
        i = {}
        i['job_name'] = response.xpath('normalize-space(.//div[@class="tHeader tHjob"]//div[@class="cn"]/h1/text())').extract_first()
        i['job_company'] = response.xpath('normalize-space(.//div[@class="tHeader tHjob"]//div[@class="cn"]/p/a/@title)').extract_first()
        i['job_area'] = response.xpath('normalize-space(.//div[@class="tHeader tHjob"]//div[@class="cn"]/span/text())').extract_first()
        i['job_price'] = response.xpath('normalize-space(.//div[@class="tHeader tHjob"]//div[@class="cn"]/strong/text())').extract_first()
        i['job_details'] = response.xpath('normalize-space(.//div[@class="tHeader tHjob"]//div[@class="cn"]/p[@class="msg ltype"]/text())').extract_first()
        i['job_url'] = response.url
        i['job_flag'] = "前程无忧"
        print(i)
        return i
        print ('\n')


#此爬虫主要是处理一页多个目标网址，然后需要翻页。  先创建一个函数处理链接问题：一个是目标的链接，一个是页面的链接
#另外一个函数主要处理目标网页的数据，并return给管道

