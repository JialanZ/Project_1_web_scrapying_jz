#import the models and items
from scrapy import Spider, Request
from movie_ratings.items import MovieRatingsItem

#set up a scrapying task in this spider file
class MovieRatingsSpider(Spider):
	name = 'movie_ratings_spider'
	allowed_urls = ['https://www.imdb.com/']    #note the name is urls dont forget the s!!!
	start_urls = ['https://www.imdb.com/search/title?year=2018&title_type=feature&sort=num_votes,desc']


	def parse(self, response):
		result_urls = ['https://www.imdb.com/search/title?year=2018&title_type=feature&sort=num_votes,desc'] + ['https://www.imdb.com/search/title?year=2018&title_type=feature&sort=num_votes,desc&page={}&ref_=adv_nxt'.format(i) for i in range(2,289)]

		for url in result_urls:
			yield Request(url=url, callback=self.parse_result_page)




	def parse_result_page(self, response):
		#xpath: movie information blocks on each page
		movie_blocks_xpath = response.xpath('//div[@class="article"]//div[@class="lister-item mode-advanced"]')
		#xpath: movie_name on each page
		movie_names_xpath = movie_blocks_xpath.xpath('.//h3[@class="lister-item-header"]/a/text()')
		#xpath: movie movie_rated blocks on each page
		movie_rateds_xpath = movie_blocks_xpath.xpath('.//p[@class="text-muted "]/span[@class="certificate"]/text()')
		#xpath: genre on each page
		movie_genres_xpath = movie_blocks_xpath.xpath('.//p[@class="text-muted "]/span[@class="genre"]/text()')
		#xpath: imdb_rating on each page
		movie_imdb_ratings_xpath = movie_blocks_xpath.xpath('.//div[@class="inline-block ratings-imdb-rating"]/strong/text()')
		#xpath: meta_rating on each page
		movie_meta_ratings_xpath = movie_blocks_xpath.xpath('.//div[@class="inline-block ratings-metascore"]/span/text()')
		#xpath: n_of_votes on each page
		movie_n_of_votes_xpath = movie_blocks_xpath.xpath('.//p[@class="sort-num_votes-visible"]/span[@name="nv"][1]/text()')
		#xpath: gross on each page
		movie_grosses_xpath = movie_blocks_xpath.xpath('.//p[@class="sort-num_votes-visible"]/span[@name="nv"][2]/text()')

		


		# print('movie_blocks_xpath length :',len(movie_blocks_xpath))
		# print('movie_names_xpath lenght:',len(movie_names_xpath))
		# print('movie_rateds_xpath length :',len(movie_rateds_xpath))
		# print('movie_genres_xpath length :',len(movie_genres_xpath))
		# print('movie_imdb_ratings_xpath length :',len(movie_imdb_ratings_xpath))
		# print('movie_meta_ratings_xpath length :',len(movie_meta_ratings_xpath))
		# print('movie_n_of_votes_xpath length :',len(movie_n_of_votes_xpath))
		# print('movie_grosses_xpath length :',len(movie_grosses_xpath))
		# print('='*50)


		for i in range(len(movie_blocks_xpath)):
		# 	print(i,movie_names_xpath[i].extract())
		# 	print(movie_rateds_xpath[i].extract())
		# 	print(movie_genres_xpath[i].extract())
		# 	print(movie_imdb_ratings_xpath[i].extract())
		# 	print(movie_meta_ratings_xpath[i].extract())
		# 	print(movie_n_of_votes_xpath[i].extract())
		# 	print(movie_grosses_xpath[i].extract())

			#should use movie blocks' index! 
			# print(i+1)
			# print(movie_blocks_xpath[i].xpath('.//h3[@class="lister-item-header"]/a/text()').extract_first())
			# print(movie_blocks_xpath[i].xpath('.//p[@class="text-muted "]/span[@class="certificate"]/text()').extract_first())
			# print(movie_blocks_xpath[i].xpath('.//p[@class="text-muted "]/span[@class="genre"]/text()').extract_first().strip())
			# print(movie_blocks_xpath[i].xpath('.//div[@class="inline-block ratings-imdb-rating"]/strong/text()').extract_first())
			# print(movie_blocks_xpath[i].xpath('.//div[@class="inline-block ratings-metascore"]/span/text()').extract_first())
			# print(movie_blocks_xpath[i].xpath('.//p[@class="sort-num_votes-visible"]/span[@name="nv"][1]/text()').extract_first())
			# print(movie_blocks_xpath[i].xpath('.//p[@class="sort-num_votes-visible"]/span[@name="nv"][2]/text()').extract_first())
			# print('='*50)

			item = MovieRatingsItem()
			item['movie_name'] = movie_blocks_xpath[i].xpath('.//h3[@class="lister-item-header"]/a/text()').extract_first()
			item['movie_rated'] = movie_blocks_xpath[i].xpath('.//p[@class="text-muted "]/span[@class="certificate"]/text()').extract_first()
			item['genre'] = movie_blocks_xpath[i].xpath('.//p[@class="text-muted "]/span[@class="genre"]/text()').extract_first().strip()
			item['imdb_rating'] = movie_blocks_xpath[i].xpath('.//div[@class="inline-block ratings-imdb-rating"]/strong/text()').extract_first()
			item['meta_rating'] = movie_blocks_xpath[i].xpath('.//div[@class="inline-block ratings-metascore"]/span/text()').extract_first()
			item['n_of_votes'] = movie_blocks_xpath[i].xpath('.//p[@class="sort-num_votes-visible"]/span[@name="nv"][1]/text()').extract_first()
			item['gross'] = movie_blocks_xpath[i].xpath('.//p[@class="sort-num_votes-visible"]/span[@name="nv"][2]/text()').extract_first()

			yield item

		#following pagination link. however it doesn't work
		# base_url = 'https://www.imdb.com/search/title'
		# if next_page_url_tail:
		# 	next_page_url_tail = response.xpath('//div[@class="desc"]/a/@href').extract_first()
		# 	next_page_url = base_url + next_page_url_tail
		# 	yield scrapy.Request(url=next_page_url, callback=self.parse_result_page)








