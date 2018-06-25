pythonjob说明文档
==
介绍
 - 
pythonjob是一个基于Scrapy的工作爬虫，目前爬取了前程无忧和智联招聘两大网站的关于python工程师的职位信息。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Faker(随机切换User-Agent)<br>

爬取结果
-
在前程无忧和智联招聘网站上总共爬取了31156条有关python工作的有效信息。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图：<br>
![](https://github.com/lanluyu/pythonjob/tree/master/pythonjob/job.PNG)

