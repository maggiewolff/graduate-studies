# Name: Maggie Wolff
# Due Date: 2/19/20
# Assignment0602_SurfCDM
# I have not given or received any unauthorized assistance on this assignment.
# Video Link: https://youtu.be/MaHHAb6Smbc


from urllib.parse import urljoin
from urllib.request import urlopen
from html.parser import HTMLParser
import re

class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http': # collect HTTP URLs
                        self.links.append(absolute)
      
    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links

    def getData(self):
        'return a list of only the words on that page'
        response = urlopen(self.url)
        content = response.read().decode().lower()
        a = re.compile(r'{.*?}')
        clean1 = a.sub('', content)
        b = re.compile(r'<.*?>')
        clean2 = b.sub('', clean1)
        words = clean2.split(' ')
        w = re.compile('^[a-z]+$')
        words = list(filter(w.match, words)) 

        return words


def crawl2(url):
    'a recursive web crawler that calls analyze() on every visited web page'

    # add url to set of visited pages
    global visited      
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)
#    global count
#    if count < 10:
#        links = analyze(url)
#        count += 1

    # recursively continue crawl from every link in links
    for link in links:
        link = link.replace('www.','')
        if link not in visited:
            try:
                if re.search('csh.depaul.edu/',link):
                    if re.search('.pdf$', link):
                        pass
                    elif re.search('#', link):
                        pass
                    elif re.search('/course-evaluations.aspx?', link):
                        pass
                    elif re.search(' ', link):
                        pass
                    else:
                        crawl2(link)
            except:
                pass



from urllib.request import urlopen
def analyze(url):
    'collect the links and the words from each webpage'

    global linkcount
    print('\nVisiting', url)           # for testing
    linkcount += 1

    # obtain links in the web page
    content = urlopen(url).read().decode().lower()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()           

    # compute word frequencies
    content = collector.getData()
#    freq = frequency(content)

    # add words to Master Word List
    global masterWordList
    global wordList
    for word in content:
        wordList.append(word)
        if word not in masterWordList:
            try:
                masterWordList.add(word)
            except:
                pass

    return urls


def frequency(words):
    'counts the instances of each word and stores in a dictionary'

    uniqueWords = set(words)
    uniqueWordsList = list(uniqueWords)
    uniqueWordsList.sort()

    wordCounts = {}

    for i in range(0, len(uniqueWordsList)):
        u = uniqueWordsList[i]
        count = 0
        for x in range (0,len(words)):
            s = words[x]
            if s == u:
                count += 1
        wordCounts[u] = count

    return wordCounts


def displayWordCounts(wordCounts):
    'display top 25 unique words with their counts' 

    print('\nRank | Count   | Word\n')
    topcount = 1
    while topcount <= 25:
        maxword = max(wordCounts, key=wordCounts.get)
        print('{:4} {:3} {:5} {:3} {:20}'.format(topcount, '|', wordCounts[maxword], '|', maxword))
        wordCounts.pop(maxword)
        topcount += 1


def main(url):
    'counts the number of words in a website and returns the 25 most frequently used'

    crawl2(url)
    print('\n\n',linkcount,'pages crawled')
    totalWordCounts = frequency(wordList)

    print('\nTop 25 Words on:',url)
    displayWordCounts(totalWordCounts)

visited = set() 
masterWordList = set()
wordList = []
count = 0 
linkcount = 0
main('http://csh.depaul.edu')

