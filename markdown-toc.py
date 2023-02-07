#! /usr/bin/env python3

import sys

def getRank(line):
    ''' (str) -> int

    Returns the rank of a given line.
    Rank will be 1 for level-1 titles (Meaning line starts with a single hash sign.)
    Rank will be 2 for level-2 titles (Meaning line starts with only two hash signs.)

    >>> getRank('#Lol')
    1
    >>> getRank('##hihi')
    2
    >>> getRank('bon ben ouais')
    0
    '''
    rank = 0
    for c in line:
        if c == '#':
            rank += 1
        else:
            break
    return rank



def makeTocEntry(line):
    ''' (str) -> str
    >>> makeTocEntry('lol')
    >>> makeTocEntry('# lol')
    '* lol'
    >>> makeTocEntry('## lolw')
    '    + lolw'
    >>> makeTocEntry('### lolwhat')
    '        - lolwhat'
    >>> makeTocEntry('#### lolwhat')
    '            * lolwhat'
    '''
    bullets = ['*', '+', '-']
    rank = getRank(line)
    if rank == 0:
        return None
    line = line[rank:].lstrip()
    pad = ' ' * ((rank-1) * 4) + bullets[(rank-1) % 3] + ' '
    return pad + line
    


def makeStub(line):
    ''' (str) -> str
    >>> makeStub('# lol')
    'lol'
    >>> makeStub('# 1 - lol')
    '1-lol'
    >>> makeStub('# 12 ! -- lol')
    '12-lol'
    >>> makeStub('# 1+ (around) - lol')
    '1-around-lol'
    '''
    out = ''
    prevIsAl = 0
    for c in line:
        if c.isalnum():
            out += c
            prevIsAl = 0
        else:
            prevIsAl += 1
            if prevIsAl == 1:
                out += '-'
    return out.strip("-")



def parseLine(line, doc, toc):
    '''(str, list of str, list of str) -> Tuple of List of str

    Parse a line and feed the necessary data into doc (representing the lines of the document) 
    and toc (representing the table of content).

    >>> doc, toc, l = [], [], 'lol\\n';parseLine(l, doc, toc); doc, toc
    (['lol'], [])
    >>> parseLine('#yo\\n', doc, toc); doc, toc
    (['lol', "<a name='yo'></a>", '#yo'], ['* yo'])
    >>> parseLine('## 2 -?y\\n', doc, toc); doc, toc
    (['lol', "<a name='yo'></a>", '#yo', "<a name='2-y'></a>", '## 2 -?y'], ['* yo', '    + 2 -?y'])
    '''
    tocE = makeTocEntry(line)
    if tocE != None:
        toc.append(tocE.rstrip())
        doc.append("<a name='" + makeStub(line) + "'></a>")
    doc.append(line.rstrip())
    

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("-t", "--test", action = 'store_true')
    p.add_argument("file", nargs = '?', default = '-')
    args = p.parse_args()

    if args.test:
        import doctest
        doctest.testmod(verbose = True)

    elif args.file:
        with args.file == '-' and sys.stdin or open(args.file) as f:
            doc, toc = [], []
            for line in f:
                parseLine(line, doc, toc)
            for line in toc:
                print(line)
            for line in doc:
                print(line)