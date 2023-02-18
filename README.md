# markdown-toc.py

A python script to generate a TOC from a Markdown file

## Self-contained

I hate how the actual markdown-toc makes you use f*cking `npm`.
That stuff is always broken and full of dependencies. 

## Specs

Here are the tech specs:

### Pass document as command line argument

### Output to stdout or to file

### Accept input from standard input

### Can be tested using the repo's README.md file.

## Usage

```bash
git clone https://github.com/epgfm/markdown-toc.py
cd markdown-toc.py
```

- Run tests
```bash
./markdown-toc.py -t
```

- Simple usage, output to file
```bash
./markdown-toc.py README.md > REDMYTOC.md
```

- Read input from STDIN
```
cat README.md | ./markdown-toc.py - 
```
