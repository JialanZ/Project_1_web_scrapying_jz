# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieRatingsDoubanItem(scrapy.Item):
	movie_name_douban=scrapy.Field()
	movie_rating_douban=scrapy.Field()
	n_of_vote_douban=scrapy.Field()


