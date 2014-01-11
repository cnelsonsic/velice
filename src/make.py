#!/usr/bin/env python
import os
from sh import pandoc
from check import check

book = []
for chapter in os.listdir('src'):
    if ".mkd" in chapter:
        with open('src/'+chapter, 'r') as f:
            text = f.read()
            book.append(text)

with open(".temp.md", 'w') as f:
    f.write('\n\n'.join(book))

pandoc = pandoc.bake('.temp.md', f='markdown',
                                 smart=True,
                                 toc=True,
                                 standalone=True,
                                 chapters=True)
pandoc(output="build/book.pdf", template="src/template")
pandoc(output="build/book.html", t="html5")
pandoc(output="build/book.odt")
pandoc(output="build/book.md", t="markdown_github")
os.unlink('.temp.md')

bads = check('\n\n'.join(book))
if bads:
    print "The following should be addressed:"
    for bad_type, bad in bads:
        print bad_type, bad
        print bad_type.title(), ":", bad
