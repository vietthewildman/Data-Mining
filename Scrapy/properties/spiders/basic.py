import scrapy
from properties.items import PropertiesItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['propzy.vn']
    start_urls = ['https://propzy.vn/mua/bat-dong-san/hcm/']


    def parse(self, response):
      
      for sel in response.xpath('//div[@class="bl-info-listing"]'):

        item = PropertiesItem()
        item['compass'] = sel.xpath('./a[position()=3]/div/span[position()=4]/text()').get()
        item['bath'] = sel.xpath('./a[position()=3]/div/span[position()=1]/text()').get().replace('\xa0','').strip()
        item['bed'] = sel.xpath('./a[position()=3]/div/span[position()=2]/text()').get().replace('\xa0','').strip()
        item['address'] = sel.xpath('./p/a[position()=1]/text()').get()
        item['ward'] = sel.xpath('./p/a[position()=2]/text()').get()
        item['dist'] = sel.xpath('./p/a[position()=3]/text()').get().replace('Quận ','').strip()
        item['area'] = sel.xpath('./a[position()=3]/div/span[position()=3]/text()').get().replace('m²','').strip()
        item['price'] = sel.xpath('./a/p/text()').get().replace('tỷ','').strip()
        item['title'] = sel.xpath('./a/h3/text()').get()
        
        yield item

      next_page = response.xpath('//div[@class="pages"]/ul/li/a[@class="next page-numbers"]/@href').get()
      # next_page = 'https://propzy.vn' + next_page
      if "/mua/bat-dong-san/hcm/p2" in next_page:
         yield response.follow(next_page, callback=self.parse)
