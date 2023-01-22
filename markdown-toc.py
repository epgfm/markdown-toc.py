#! /usr/bin/env python3

print("Hello")

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
    '''
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
    




def parseLine(line, doc, toc):
    '''(str, list of str, list of str) -> Tuple of List of str

    Parse a line and feed the necessary data into doc (representing the lines of the document) 
    and toc (representing the table of content).

    >>> doc, toc, l = [], [], 'lol\\n';parseLine(l, doc, toc); doc, toc
    (['lol\\n'], [])
    >>> parseLine('#yo\\n', doc, toc); doc, toc
    (['lol\\n', '#yo\\n'], ['* yo\\n'])
    '''
    doc.append(line)
    tocE = makeTocEntry(line)
    if tocE != None:
        toc.append(tocE)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("-t", "--test", action = 'store_true')
    args = p.parse_args()

    if args.test:
        import doctest
        doctest.testmod(verbose = True)


