import secretKeys as sk
from xml.etree import ElementTree 
from rauth.service import OAuth1Service, OAuth1Session

goodreads = OAuth1Service(
    consumer_key=sk.CONSUMER_KEY,
    consumer_secret=sk.CONSUMER_SECRET,
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

print request_token
print request_token_secret

session = goodreads.get_auth_session(request_token, request_token_secret)

params = {'v': 2,
          'key': CONSUMER_KEY,
          'shelf': 'read'}

response = session.get('https://www.goodreads.com/review/list.xml?', params=params).content

print response
tree = ElementTree.fromstring(response)


    

