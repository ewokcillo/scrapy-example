# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from opendata.items import MemberItem


class CongresoSpider(CrawlSpider):
    name = "congreso"
    allowed_domains = ["congreso.es"]
    start_urls = (
        'http://www.congreso.es/portal/page/portal/Congreso/Congreso/Diputados',
    )

    rules = (
        Rule(LinkExtractor(allow=r'fichaDiputado'), callback='parse_member'),
        Rule(LinkExtractor(allow=r'Diputados'), follow=True)
    )

    def parse_member(self, response):
        loader = ItemLoader(item=MemberItem(), response=response)
        loader.add_xpath('name', '//div[@class="nombre_dip"]/text()')
        loader.add_xpath('term', '//div[@id="curriculum"]/div[@class="principal"]/text()')
        loader.add_xpath('province', '//div[@class="texto_dip"]/ul/li/div[@class="dip_rojo"]/text()')
        loader.add_xpath('party', '//div[@class="texto_dip"]/ul/li/div[@class="dip_rojo"]/a/text()')
        yield loader.load_item()
