import scrapy
import pandas as pd


class TwitchSpider(scrapy.Spider):
	name = 'comp-spider'
	start_urls = ['https://www.konux.com/about-us/', 'https://www.asiabots.com/team']

	def parse(self, response):
		if response.url == 'https://www.konux.com/about-us/':
			founder = response.xpath('//h5[1]/text()').extract()
			posi = response.xpath('//h5[1]/following-sibling::p/text()').extract()
			pd.DataFrame([founder, posi]).T.to_csv('konus.csv')
		elif response.url == 'https://www.asiabots.com/team':
			founder_ab = response.xpath('//div[@class="s-component-content s-font-body"]/p[1]/text()').extract()
			pd.DataFrame(founder_ab).to_csv('asiabots.csv')
		
		yield None