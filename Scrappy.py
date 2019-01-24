import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://www.hirunews.lk/', 'http://www.hirunews.lk/local-news.php', 'http://www.hirunews.lk/entertainment/',
        'http://www.hirunews.lk/international-news.php', 'http://www.hirunews.lk/sports/',
        'http://www.hirunews.lk/business/'
    ]

    def parse(self, response):
        for quote in response.css('.rp-mian'):
            yield {
                'header': quote.css('.lts-cntp a::text').extract_first(),
                'content': quote.css('.lts-txt2::text').extract_first(),
                'tags': quote.css('.lts-txt2::text').extract(),
            }


#scrapy runspider Scrappy.py -o out.csv
