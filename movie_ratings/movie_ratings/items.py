# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieRatingsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name=scrapy.Field()
    movie_rated=scrapy.Field()
    genre=scrapy.Field()
    imdb_rating=scrapy.Field()
    meta_rating=scrapy.Field()
    n_of_votes=scrapy.Field()
    gross=scrapy.Field()

