
import re
import sys


# a ConstitTree consists of a category label 'c' and a list of child Trees 'ch'
class ConstitTree:

    # obtain tree from string
    def read(this, s):
        this.ch = []
        # a tree can be just a terminal symbol (a leaf)
        m = re.search('^ *([^ ()]+) *(.*)', s)
        if m != None:
            this.c = m.group(1)
            return m.group(2)
        # a tree can be an open paren, nonterminal symbol, subtrees, close paren
        m = re.search('^ *\( *([^ ()]*) *(.*)', s)
        if m != None:
            this.c = m.group(1)
            s = m.group(2)
            while re.search('^ *\)', s) == None:
                t = ConstitTree()
                s = t.read(s)
                this.ch = this.ch + [t]
            return re.search('^ *\) *(.*)', s).group(1)
        return ''

    # obtain consist-marked string from tree
    def str(this):
        if this.ch == []:
            return this.c
        if len(this.ch) > 1:
            s = '<constit> '
        else:
            s = ''
        for t in this.ch:
            s = s + ' ' + t.str()
        if len(this.ch) > 1:
            s = s + ' </constit>'
        return s

for line in sys.stdin:
    while line != '':
        t = ConstitTree()
        line = t.read(line)
        print(t.str())


