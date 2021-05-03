import requests
import logging
import time

from pages.all_books_page import AllBooksPage


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')

print('Loading book list')
logger.info('Loading books list.')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('http://books.toscrape.com').content

logger.debug('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

books = page.books

for book in books:
    print(book)
