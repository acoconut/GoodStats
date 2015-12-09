import secretKeys as SK
import xml.etree.ElementTree as ET
from rauth.service import OAuth1Service, OAuth1Session

BOOKS_PER_PAGE = 200 # Number of books to be retrieved at once. Max=200

goodreads = OAuth1Service(
    consumer_key=SK.CONSUMER_KEY,
    consumer_secret=SK.CONSUMER_SECRET,
    name='goodreads',
    request_token_url='http://www.goodreads.com/oauth/request_token',
    authorize_url='http://www.goodreads.com/oauth/authorize',
    access_token_url='http://www.goodreads.com/oauth/access_token',
    base_url='http://www.goodreads.com'
    )

request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

#Exchanging our request token for an access token
authorize_url = goodreads.get_authorize_url(request_token)
print 'Visit this URL in your browser: ' + authorize_url
accepted = 'n'
while accepted.lower() == 'n':
    # you need to access the authorize_link via a browser,
    # and proceed to manually authorize the consumer
    accepted = raw_input('Have you authorized me? (y/n) ')

session = goodreads.get_auth_session(request_token, request_token_secret)

cont = BOOKS_PER_PAGE #to check if we retrieve 200 books
page = 0

books = []
while cont == BOOKS_PER_PAGE:
    cont = 0
    params = {'v': 2,
              'key': SK.CONSUMER_KEY,
              'page': page,
              'shelf': 'read',
              'per_page': BOOKS_PER_PAGE}

    response = session.get('https://www.goodreads.com/review/list.xml?', params=params).content
    root = ET.fromstring(response)

    page = page + 1

    for book in root.iter('book'):
        books.append([book.find('title').text])
        print book.find('title').text
        cont = cont +1

print cont
    
