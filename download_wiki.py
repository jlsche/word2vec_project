import urllib.request

# EN wiki
url = 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles-multistream.xml.bz2'
urllib.request.urlretrieve(url, 'enwiki-latest-pages-articles-multistream.xml.bz2')

# CH wiki
#url = 'https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2'
#resp = urllib.request.urlretrieve(url, 'zhwiki-latest-pages-article.xml.bz2')
