import logging

from crawler.crawler import Crawler
from crawler.downloader import SeleniumHTMLDownloader
from crawler.parse.ynet import YnetParser
from crawler.store import MongoArticleStore


def main():
    _setup_logging()
    downloader = SeleniumHTMLDownloader('./lib/chromedriver.exe')
    store = MongoArticleStore("localhost", 27017, "Crawler", "Articles")
    crawler = Crawler(downloader, {
        'ynet.co.il': YnetParser()
    }, store)
    crawler.crawl('https://www.ynet.co.il')


def _setup_logging():
    # create logger
    logger = logging.getLogger('crawler')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)


if __name__ == '__main__':
    main()
