import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # with open('resultados.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        title = response.xpath('//title/text()').get()
        tags = response.xpath('//a[@class="tag"]/text()').getall()
        c = 1
        correctTags = list(set(tags))
        for tag in correctTags:
            c += 1
        # JSON: scrapy crawl quotes -o quotes.json
        # CSV   scrapy crawl quotes -o quotes.csv
        yield {
            'title': title,
            'tags': tags
        }