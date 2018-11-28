from abc import ABCMeta, abstractmethod

from bs4 import BeautifulSoup
from typing import List

from models import Article


class HTMLDownloaderBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def download(self, url):
        # type: (str) -> BeautifulSoup
        pass


class TargetExtractorBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def extract_targets(self, node, article, current_url):
        # type: (BeautifulSoup, Article, str) -> List[str]
        pass


class ArticleParserBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, node, url):
        # type: (BeautifulSoup, str) -> Article
        pass


class ArticleStoreBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def store(self, article):
        # type: (Article) -> None
        pass


class CrawlerBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def crawl(self, url):
        # type: (str) -> None
        pass
