import re
import logging

from locators.all_books_page import AllBooksPageLocators
from parsers.book import BookParser
from bs4 import BeautifulSoup

logger = logging.getLogger('scraping.all_books_page')

class AllBooksPage:
    def __init__(self,page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in a page using `{AllBooksPageLocators.BOOKS}')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]



