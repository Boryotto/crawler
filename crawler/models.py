class Article:
    def __init__(self, url, title, subtitle, author, date, body):
        self.subtitle = subtitle
        self.url = url
        self.body = body
        self.date = date
        self.author = author
        self.title = title


class MongoConfiguration(object):
    def __init__(self, host, port, username=None, password=None):
        self.port = port
        self.password = password
        self.username = username
        self.host = host
