# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ZhilianSpider(CrawlSpider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%85%a8%e5%9b%bd&kw=python&sm=0&isfilter=0&fl=489&isadv=0&sg=b6f80cec18f64006a4d58713686c317e&p=2']

    def parse(self,response):  #此response为每一页的响应
        #获取每一页的工作详情链接
        links = response.xpath('.//td[@class="zwmc"]//a/@href').extract()
        for link in links:
            yield scrapy.Request(link,callback=self.parse_job)

        
        #获取下一页的链接
        next_url = response.xpath('.//div[@class = "pagesDown"]//li/a[contains(text(),"下一页")]/@href').extract_first()
        #将下一页的链接丢给parse函数处理，继续得到工作详情链接和下一页链接
        yield scrapy.Request(next_url,callback=self.parse)
        print ("----------------下一页------------------") 
        print (response.url)
        print ('\n')
      
    #定义处理工作详情页面的函数 parse_job
    def parse_job(self, response):   #此处的response为工作详情页面的响应内容
        #print ("----------------Start------------------") 
        print (response.url)
        i = {}
        i['job_name'] = response.xpath('normalize-space(.//div[@class="fixed-inner-box"]/div/h1/text())').extract_first()
        i['job_company'] = response.xpath('normalize-space(.//div[@class="fixed-inner-box"]/div/h2/a/text())').extract_first()
        i['job_area'] = response.xpath('normalize-space(.//span[contains(text(),"工作地点")]/../strong/a/text())').extract_first()
        i['job_price'] = response.xpath('normalize-space(.//span[contains(text(),"职位月薪")]/../strong/text())').extract_first()
        i['job_details'] = response.xpath('normalize-space(.//span[contains(text(),"公司行业")]/../strong/a/text())').extract_first()
        i['job_url'] = response.url
        i['job_flag'] = "智联招聘"
        print(i)
        return i
        print ('\n')



    
