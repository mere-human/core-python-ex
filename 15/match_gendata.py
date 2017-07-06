import re
import os

def match_days(data):
    patt = r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
    #patt = r'^(\w{3})'
    m = re.match(patt, data)
    if m is not None:
        print(m.group())

def search_integers(data):
    patt = r'\d+-\d+-\d+'
    m = re.search(patt, data)
    if m is not None:
        print(m.group())

def match_integers_greedy(data):
    patt = r'.+(\d+-\d+-\d+)'
    m = re.search(patt, data)
    if m is not None:
        print(m.group(1))

def match_integers_non_greedy(data):
    patt = r'.+?(\d+-\d+-\d+)'
    m = re.search(patt, data)
    if m is not None:
        print(m.group(1))

def main():
    with os.popen('gendata.py', 'r') as f:
        line = f.readline()
        print(line)
        match_days(line)
        search_integers(line)
        match_integers_greedy(line)
        match_integers_non_greedy(line)

if __name__ == '__main__':
    main()