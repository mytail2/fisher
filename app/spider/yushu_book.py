#!/usr/bin/env python
from app.libs.httper import Http
from flask import current_app


class YuShuBook:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        isbn_url = cls.isbn_url.format(isbn)
        result = Http.get(isbn_url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page):
        keyword_url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = Http.get(keyword_url)
        return result

    @staticmethod
    def calculate_start(page):
        return current_app.config['PER_PAGE']*(page-1)
