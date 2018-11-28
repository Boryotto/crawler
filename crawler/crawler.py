import logging
import re

from typing import Mapping, Optional

from abstractions import CrawlerBase
from abstractions import HTMLDownloaderBase, ArticleStoreBase
from parse.abstractions import WebsiteParserBase

LOGGER = logging.getLogger(__name__)


class Crawler(CrawlerBase):

    def __init__(self, downloader, parser_mapping, article_store):
        # type: (HTMLDownloaderBase, Mapping[str, WebsiteParserBase], ArticleStoreBase) -> None
        self.article_store = article_store
        self.parser_mapping = parser_mapping
        self.downloader = downloader

    def crawl(self, url):
        urls_to_crawl = [url]
        while len(urls_to_crawl) > 0:
            collected_targets = []
            for url in urls_to_crawl:
                LOGGER.info("Searching for a matching parser. URL: %s", url)
                parser = self._get_matching_parser(url)
                if parser is not None:
                    LOGGER.info("Downloading web page. URL: %s", url)
                    page_node = self.downloader.download(url)
                    LOGGER.info("Parsing web page to Article. URL: %s", url)
                    article = parser.parse(page_node, url)
                    if article:
                        self.article_store.store(article)
                    else:
                        LOGGER.info("No article could be parsed from web page. URL: %s", url)
                    next_targets = parser.extract_targets(node=page_node, article=article,
                                                          current_url=url)
                    collected_targets.extend(next_targets)
                else:
                    LOGGER.info("No parser was found for the url. skipping. URL: %s", url)
            urls_to_crawl = collected_targets

    def _get_matching_parser(self, link):
        # type: (str) -> Optional[WebsiteParserBase]
        for pattern, parser in self.parser_mapping.iteritems():
            try:
                if re.search(pattern, link) is not None:
                    return parser
            except re.error as ex:
                LOGGER.warning('Parser regex is not valid!. parser_type: %s, reason: %s', parser.__class__.__name__,
                               ex.message)
        return None
