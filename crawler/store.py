import logging

import pymongo

from abstractions import ArticleStoreBase

LOGGER = logging.getLogger(__name__)


class MongoArticleStore(ArticleStoreBase):
    def __init__(self, host, port, db, article_collection, username=None, password=None):
        self.password = password
        self.username = username
        self.article_collection = article_collection
        self.db = db
        self.port = port
        self.host = host
        LOGGER.info("Connecting to DB... %s:%s", host, port)
        self.client = pymongo.MongoClient(host=host, port=port, username=username, password=password)
        LOGGER.info("Connected to DB.")
        self.db = self.client[db]

    def store(self, article):
        LOGGER.info("Storing article to db. URL: %s", article.url)
        self.db[self.article_collection].insert_one(vars(article))
