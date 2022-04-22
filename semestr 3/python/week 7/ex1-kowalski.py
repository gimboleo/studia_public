'''
DISCLAIMER

Part of the task was to implement a function that outputs all sentences containing the word "Python".
I tested my solution on real websites and sentence-tokenizing (without greatly dumbing down the definition of a sentence) is a really
complicated and tricky problem, so implementing a passable solution proved to be a bit out of my league. (for instance, all
possible regex shenanigans I came up with weren't even near being satisfactory) Thus, I implemented 2 different solutions mitigating
this problem:
    1. Using the Natural Language Toolkit - a very robust library for working with human language data
    2. Treating whole blocks of text as sentences.

DISCLAIMER II: Comments added in the new version start with 2 hashes (##)
'''



#All external libraries can be installed using pip

#I use an external library for pulling data out of html files called Beautiful Soup
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#It was shown on the fifth lecture
from bs4 import BeautifulSoup
from bs4.element import Comment

#I also use an external library for sending HTTP requests called requests
#https://docs.python-requests.org/en/latest/
import requests

#Natural Language Toolkit
#https://www.nltk.org/index.html
import nltk
nltk.download('punkt')   
print("\n\n")      
#The library needs to download the punkt package (a tokenizer) for the nltk solution to work properly

from urllib.parse import urlparse, urljoin
import time

##Concurrent.futures provides a high-level interface for asynchronously executing callables (using threads or processes)
import concurrent.futures as cf



def crawl(start_page, distance, action):
    '''
    start_page should be a string containing the url
    action should be a function taking an url in the string form
    '''

    #to_visit contains urls that are to be visited in the next depth level
    to_visit = {start_page}
    #visited represents urls visited so far
    visited = set()


    #During testing it became apparent that not all anchors (<a> in html) are valid urls
    #(these anchors mainly contained javascript)
    #So I made a function that checks if an url is in fact, a valid url
    def valid_url(url):
        #urllib.parse.urlparse divides an url into 6 segments: <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        parsed = urlparse(url)
        #I use it to check if given url contains a scheme (protocol name) and netloc (domain, subdomain, etc.)
        #Additionaly the function broke when it encountered a mailto protocol
        return parsed.netloc and parsed.scheme and parsed.scheme != "mailto"


    def aux(url):
        '''
        This function handles scraping - it visits an url from to_visit and searches for valid urls in it
        When it's done, it returns the found set
        '''

        found = set()

        soup = BeautifulSoup(requests.get(url).content, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            #Some tags can be empty and we don't want them
            if not href: continue

            #extracted urls can be (and often are) relative
            #urllib.parse.urljoin constructs an absolute url by combining a base url with another url if the latter is relative
            href = urljoin(url, href)
            #Urls that have the same scheme, netloc and path segments but differ in params, query and fragment segments are
            #considered the same website (For example: On a website there can be a link that moves the user to another part
            #of the same website, using an id of a element in the anchor. This would be represented as #id at the end of the url)
            #(for more info please go to https://stackoverflow.com/questions/53992694/what-does-netloc-mean)
            parsed = urlparse(href)
            #So we reconstruct the url without the unneeded segments to get rid of a possible redundancy in the found set
            href = parsed.scheme + "://" + parsed.netloc + parsed.path

            if valid_url(href) and href not in visited: found.add(href)

        return found


    def generator_generator():
        '''
        This function generates generators for each depth of the search.
        '''
        
        nonlocal to_visit

        ##ThreadPoolExecutor uses a pool of threads to execute code asynchronously
        ##By default, it uses min(32, os.cpu_count() + 4) threads
        with cf.ThreadPoolExecutor() as executor:
            for i in range(distance + 1):
                ##Future objects encapsulate the asynchronous execution and are created using executor.submit
                ##In this dictinary we hold Future objects calculating a given action as keys and urls they use as values
                actions = {executor.submit(action, url): url for url in to_visit}
                visited.update(to_visit)
                ##executor.map works kinda like a normal map but executes a function on the iterable asynchronously
                if i < distance: to_visit = set().union(*list(executor.map(lambda url: aux(url), to_visit)))
                ##as_completed yields Future objects as they complete their computations
                yield ((actions[f], f.result()) for f in cf.as_completed(actions))


    ##The main function yields values from generators yielded by the function above
    for gen in generator_generator(): yield from gen



##As promised, I made it so that the sentence tokenizing doesn't include an occasional dose of html / javascript
##The downside is, if a sentence is spread across a few html elements, it will be split and treated as multiple elements
##It can be seen especially on Wikipedia, because of an absurd amount of inline links.
##I didn't really know how to avoid both problems in a consistent way.


def tag_filter(element):
    "This function is for omitting several html elements that we definitely don't want to consider in our search"

    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: return False
    if isinstance(element, Comment): return False
    return True


def sentences_containing_nltk(phrase, url):
    "Finds a list of sentences from the url that contain a given phrase. Uses nltk"

    res = []

    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    #We divide all text from the url into an array of strings
    text = filter(tag_filter, soup.findAll(text = True))

    for block in text:
        #nltk.tokenize.sent_tokenize tokenizes a given string into sentences
        for sentence in nltk.tokenize.sent_tokenize(block): 
            if phrase in sentence: res.append(sentence)
    
    return res
contains_Python_nltk = lambda x: sentences_containing_nltk("Python", x)



def blocks_containing(phrase, url):
    '''
    Finds a list of sentences from the url that contain a given phrase. Treats blocks of text as sentences
    This solution is far from perfect (for example it will often split one sentence into multiple if it's spread across multiple blocks
    [for example if a part of text is a link nested in an anchor])
    '''
    
    res = []

    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    text = filter(tag_filter, soup.findAll(text = True))

    for block in text:
        if phrase in block: res.append(block)
    
    return res
contains_Python_block = lambda x: blocks_containing("Python", x)


#A simple action that gets the title of a given website
def get_title(url): return BeautifulSoup(requests.get(url).content, "html.parser").title.string



#TESTING ZONE#
'''
print("Block tokenizing:")
start = time.time()
print(blocks_containing("Python", "https://www.python.org")[10:20]) #I used slicing for the test to be more readable as the result is big
print("--- %s seconds ---" % (time.time() - start))
print("\n\n")
print("Nltk tokenizing:")
start = time.time()
print(contains_Python_nltk("https://www.python.org/")[10:20])
print("--- %s seconds ---" % (time.time() - start))
print("\n\n")

print("Wikipedia crawling - printing out the titles")
start = time.time()
for x in crawl("https://en.wikipedia.org/wiki/Main_Page", 0, get_title): print(x)
print("--- %s seconds ---" % (time.time() - start))
print("\n\n")
#The wikipedia main page contains a huge amount of links and it can take some time to crawl (~100s in my case), even with depth 1
start = time.time()
for x in crawl("https://en.wikipedia.org/wiki/Main_Page", 1, get_title): print(x)
print("--- %s seconds ---" % (time.time() - start))
print("\n\n")
'''

'''
print("Wikipedia crawling - Python")
start = time.time()
for x in crawl("https://en.wikipedia.org/wiki/Main_Page", 1, contains_Python_nltk): 
    if x[1]: print(x)
print("--- %s seconds ---" % (time.time() - start))
print("\n\n")
'''

'''
#An old website I found that doesn't have that many links in it
start = time.time()
for x in crawl("http://acme.com/", 1, lambda x: sentences_containing_nltk("Java", x)): 
    if x[1]: print(x)
print("--- %s seconds ---" % (time.time() - start))
print("\n\n")
'''

#Generally this implementation isn't that fast and due to the massive amount of additional links to check at each next depth,
#it won't finish in a sensible time for distance > 1 if used on the Internet and not a self-contained system.
#Maybe limiting the amount of links it can visit instead of limiting the depth of search would be a good idea

#I think this code could be optimised to run much better but I ran out of time as I had to focus on other courses :c


##This example shows the problem explained in the line 125 (splitting sentences because of inline links)
'''
start = time.time()
for i in contains_Python_nltk("https://en.wikipedia.org/wiki/Pythonesque_(play)"): print(i)
print("--- %s seconds ---" % (time.time() - start))
print("\n\n")
'''

start = time.time()
for x in crawl("https://sites.google.com/cs.uni.wroc.pl/boehm/python_parsing", 2, contains_Python_nltk): print(x)
print("--- %s seconds ---" % (time.time() - start))
print("\n\n")


##Adding concurrency to this solution made it a little bit faster but not as much as I thought it would
##I'm genuinely not sure why that's the case but perhaps it's due to GIL
##The only bottleneck saved is waiting for the I/O operations to finish
##https://wiki.python.org/moin/GlobalInterpreterLock