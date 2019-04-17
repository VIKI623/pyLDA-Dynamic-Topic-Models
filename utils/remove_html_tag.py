# coding: utf-8
from re import sub
from sys import stderr
# need download https://pypi.org/project/micropython-_markupbase/3.3.3-1/#files,
# and copy _markupbase.py to \Lib\site-packages, then rename it to markupbase.py
# this library make html content to be right format
# 不能直接使用HTMLParser，而是用html.parser，
# 否则如果环境是python3.x，会遇到兼容问题
# from HTMLParser import HTMLParser
from html.parser import HTMLParser
from traceback import print_exc
from bs4 import BeautifulSoup

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')
        elif tag == 'div':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()

def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        #If invoke exception, then return text by beautifulsoup
        soup = BeautifulSoup(text, 'html.parser')
        return soup.text