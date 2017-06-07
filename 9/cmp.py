'''
9-6. File Comparison. Write a program to compare two text files. If they are different, give
the line and column numbers in the files where the first difference occurs.
'''

import sys

def read_lines(name):
    f = open(name, 'r')
    lines = f.readlines()
    f.close()
    return lines

def find_first_diff_char(str1, str2):
    if str1 == str2:
        return -1
    chars_count = min(len(str1), len(str2))
    for i in range(chars_count):
        if str1[i] != str2[i]:
            return i
    return len(str2) if i == len(str1) else len(str1)

def main():
    fname1, fname2 = sys.argv[1], sys.argv[2]
    lines1 = read_lines(fname1)
    lines2 = read_lines(fname2)
    lines_count = min(len(lines1), len(lines2))
    for i in range(lines_count):
        col_diff = find_first_diff_char(lines1[i], lines2[i])
        if col_diff >= 0:
            print('Diff at line %d, column %d' % (i, col_diff))

if __name__ == '__main__':
    main()
