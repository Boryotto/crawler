import re
from datetime import datetime
from urlparse import urljoin

from crawler.models import Article
from crawler.parse.abstractions import WebsiteParserBase


class YnetParser(WebsiteParserBase):
    def parse(self, node, url):
        if re.search('ynet.co.il/articles', url) is not None:
            p_tags = node.find("div", class_="art_body").div.span.findAll('p')
            # TODO: query out p that includes link or script childrens
            body = reduce(lambda result, tag: "\n".join([result, tag.text]), p_tags, '')
            metadata_node = node.find('div', class_="art_header")
            title = metadata_node.find(class_='art_header_title').text
            meta_footer = metadata_node.findAll(class_='art_header_footer_author')
            author = meta_footer[0].text.strip()
            date_str = meta_footer[1].text.strip()[8:]
            date = datetime.strptime(date_str, "%d.%m.%y , %H:%M")
            subtitle = metadata_node.find(class_='art_header_sub_title').text
            return Article(url, title, subtitle, author, date, body)
        return None

    def extract_targets(self, node, article, current_url):
        return [urljoin(current_url, tag['href']) for tag in node.findAll(href=re.compile('articles'))]
