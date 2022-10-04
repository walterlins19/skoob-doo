# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


class ReviewsSkoob(scrapy.Spider):
    name = "reviewsSkoob"

    def start_requests(self):

        urls = ["https://www.skoob.com.br/livro/resenhas/" + str(i) for i in range(1, 456920)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
