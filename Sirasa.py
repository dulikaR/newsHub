import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://newsfirst.lk/sinhala/category/WORLD', 'http://newsfirst.lk/sinhala/category/SPORTS', 'http://newsfirst.lk/sinhala/category/BUSINESS',
        'http://newsfirst.lk/sinhala/category/ENTERTAINMENT', 'http://newsfirst.lk/sinhala/category/science'
    ]

    def parse(self, response):
        for quoteURL in response.css('.read-more::attr(href)').extract():
            print quoteURL
            yield scrapy.Request( quoteURL, callback=self.parse_product )
    def parse_product(self, response):
         yield {
            'header': response.css( '.post-title::text' ).extract_first(),
            'content': response.css( '#post-content p::text' ).extract_first(),
            }

#scrapy runspider Scrappy.py -o out.csv
