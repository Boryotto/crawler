from abc import ABCMeta

from crawler.abstractions import TargetExtractorBase, ArticleParserBase


class WebsiteParserBase(TargetExtractorBase, ArticleParserBase):
    __metaclass__ = ABCMeta
    pass
