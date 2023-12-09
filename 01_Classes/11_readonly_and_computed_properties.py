'''
to create a read only property we need to create a property with only
get accessor defined
'''
import math
from tracemalloc import start
class Circle:
    def __init__(self, r):
        self._r = r

    @property
    def area(self):
        return math.pi * self._r * self._r
    
c = Circle(10)
if False:
    c.area = 10 # will throw AttributeError Exception
print(c.area)


'''
Application : Caching Computed Properties (in this case, circle area)
'''
class Circle:
    def __init__(self, r) -> None:
        self._r = r
        self._area = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError('Radius must be greater than zero')
        self._r = r
        self._area = None # setting _area as None as soon as we receive valid radius (invalidating cached area)

    @property
    def area(self):
        if self._area is None:
            print('Calculating area')
            self._area = math.pi * self.radius * self.radius
        return self._area

c = Circle(10)
c.radius = 15
print(c.area)
print(c.area)


'''
Application : Caching Computed Properties (in this case, web page info)
'''

from urllib import request
from time import perf_counter
class WebPage:
    def __init__(self, url):
        self.url = url
        self._page = None
        self._page_size = None
        self._load_time_secs = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self,url):
        self._url = url
        self._page = None
    
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page

    @property
    def page_size(self):
        if self._page_size is None:
            self.download_page()
        return self._page_size

    @property
    def load_time(self):
        if self._load_time_secs is None:
            self.download_page()
        return self._load_time_secs

    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with request.urlopen(self.url) as f:
            self._page = f.read()

        end_time = perf_counter()
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time

urls = [
    'https://www.google.com/',
    'https://www.python.org/'
]

for url in urls:
    obj = WebPage(url)
    print(f'{url} \tsize={obj.page_size}\telapsed time={obj.load_time}')