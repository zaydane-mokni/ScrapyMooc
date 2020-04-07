# -*- coding: utf-8 -*-
import scrapy

filename = 'courses_details.txt'

class CoursesDetailsSpider(scrapy.Spider):
    name = 'courses_details'
    start_urls = ['http://www.france-galop.com/en/racing/meeting/20200329/QzRsYU1WMUhSb05sUzQ4UzZVdGVXZz09']

    def parse(self, response):
        courses_names = response.xpath(
        '//*[@id="block-system-main"]/div/div/div[2]/table/tbody/tr[*]/td[3]/a/text()').extract()
        courses_distance = response.xpath(
        '//*[@id="block-system-main"]/div/div/div[2]/table/tbody/tr[*]/td[5]/text()').extract()
        course_prizeMoney = response.xpath(
        '//*[@id="block-system-main"]/div/div/div[2]/table/tbody/tr[*]/td[9]/text()').extract()
        count = len(courses_names)

        with open(filename, '+a') as file:
             for i in range (0,count) :
                 file.write(courses_names[i] +' , ' + courses_distance[i] +' , ' + course_prizeMoney[i])
                 print(courses_names[i] +' , ' + courses_distance[i] +' , ' + course_prizeMoney[i])
