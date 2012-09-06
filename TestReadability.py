#-------------------------------------------------------------------------------
# Name:        TestReadability
# Purpose:
#
# Author:      Mykola
#
# Created:     31.08.2012
# Copyright:   (c) Mykola 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from readability.readability import Document
import urllib

def main():
    html = urllib.urlopen("http://habrahabr.ru/post/150756/").read()
    doc = Document(html)
    short_title = doc.short_title()
    readable_article = doc.summary()
    f = open("C:\\users\\mykola\\documents\\%s.html" % short_title, "wb")
    f.write(readable_article.encode("utf-8"))
    f.close()

if __name__ == '__main__':
    main()
