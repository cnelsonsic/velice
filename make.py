#!/usr/bin/env python
import os
from sh import pandoc
from check import check

book = []
for chapter in os.listdir('.'):
    if ".mkd" in chapter:
        with open(chapter, 'r') as f:
            text = f.read()
            book.append(text)

with open(".temp.md", 'w') as f:
    f.write('\n\n'.join(book))

pandoc = pandoc.bake('.temp.md', f='markdown',
                                 smart=True,
                                 toc=True,
                                 standalone=True,
                                 chapters=True)
pandoc(output="book.pdf", template="template")
pandoc(output="book.html", t="html5")
pandoc(output="book.odt")
pandoc(output="book.md", t="markdown_github")
os.unlink('.temp.md')

bads = check('\n\n'.join(book))
if bads:
    print "The following should be addressed:"
    for bad_type, bad in bads:
        print bad_type, bad
        print bad_type.title(), ":", bad
