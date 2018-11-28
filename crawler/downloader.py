from bs4 import BeautifulSoup
from selenium import webdriver

from abstractions import HTMLDownloaderBase


class SeleniumHTMLDownloader(HTMLDownloaderBase):

    def __init__(self, webdriver_path):
        self.webdriver_path = webdriver_path
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1200x600')

    def download(self, url):
        driver = webdriver.Chrome(self.webdriver_path, chrome_options=self.options)
        driver.get(url)
        html = driver.page_source
        return BeautifulSoup(html, 'html.parser')
