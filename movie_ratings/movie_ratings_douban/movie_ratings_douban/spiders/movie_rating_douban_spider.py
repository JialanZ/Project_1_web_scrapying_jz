#import the models and items
from scrapy import Spider, Request
from movie_ratings_douban.items import MovieRatingsDoubanItem

#set up a scrapying task in this spider file
class MovieRatingsDoubanSpider(Spider):
	name = 'movie_rating_douban_spider'
	allowed_urls = ['https://www.douban.com/']    #note the name is urls dont forget the s!!!
	start_urls = ['https://movie.douban.com/tag/2018%20%E7%BE%8E%E5%9B%BD?type=O']


#403 forbidden. this method add user agent heads to each url to get response from the websites
	def start_requests(self):
		headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
		for url in self.start_urls:
			yield Request(url, headers=headers)
		for url in self.allowed_urls:
			yield Request(url, headers=headers)

	def parse(self, response):
		headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
		result_urls = ['https://movie.douban.com/tag/2018%20%E7%BE%8E%E5%9B%BD?type=O'] + ['https://movie.douban.com/tag/2018%20%E7%BE%8E%E5%9B%BD?start={}&type=O'.format(i*20) for i in range(1,36)]

		for url in result_urls:
			yield Request(url=url, headers=headers, callback=self.parse_result_page)


	def parse_result_page(self, response):
		headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
		movie_blocks_path = response.xpath('//div[@class]//div[@class="pl2"]')
		movie_detail_urls = movie_blocks_path.xpath('./a/@href').extract()   #list of movie subpages

		for url in movie_detail_urls:
			yield Request(url, headers=headers, callback=self.parse_detail_page)

	def parse_detail_page(self, response):
		movie_name=response.xpath('//div[@id="wrapper"]//span[@property="v:itemreviewed"]/text()').extract_first()
		movie_rating=response.xpath('//div[@id="wrapper"]//strong[@class="ll rating_num"]/text()').extract_first()
		num_votes=response.xpath('//div[@id="wrapper"]//a[@class="rating_people"]/span/text()').extract_first()
		# print('='*50)
		# print(movie_name)
		# print(movie_rating)
		# print(num_votes)
		# print('='*50)
		item = MovieRatingsDoubanItem()
		item['movie_name_douban'] = movie_name
		item['movie_rating_douban'] = movie_rating
		item['n_of_vote_douban'] = num_votes

		yield item
		# result_urls = ['https://www.imdb.com/search/title?year=2018&title_type=feature&sort=num_votes,desc'] + ['https://www.imdb.com/search/title?year=2018&title_type=feature&sort=num_votes,desc&page={}&ref_=adv_nxt'.format(i) for i in range(2,289)]

		# for url in result_urls:
		# 	yield Request(url=url, callback=self.parse_result_page)



		# print('='*50)
		# print(movie_detail_urls)
		# print('='*50)