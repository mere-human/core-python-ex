'''
9-16. Text Processing. You are tired of seeing lines on your e-mail wrap because people type
lines that are too long for your mail reader application. Create a program to scan a
text file for all lines longer than 80 characters. For each of the offending lines, find the
closest word before 80 characters and break the line there, inserting the remaining
text to the next line (and pushing the previous next line down one). When you are
done, there should be no lines longer than 80 characters.
'''

import sys
import os.path

def find_last_word_pos(text, start=None):
    if start is None:
        start = len(text)-1
    has_nonspace = False
    i = start
    while i > 0:
        if text[i].isspace():
            if has_nonspace:
                break
        else:
            has_nonspace = True
        i -= 1
    return i

def split_long_lines(input_seq, max_line_len=80):
    lines = []
    for index, line in enumerate(input_seq):
        if len(line) > max_line_len:
            last_word_pos = find_last_word_pos(line)
            while last_word_pos > 0 and last_word_pos > max_line_len:
                last_word_pos = find_last_word_pos(line, last_word_pos)
            if last_word_pos > 0:
                lines.append(line[:last_word_pos-1]+'\n')
                lines.append(line[last_word_pos:])
            else:
                lines.append(line)
        else:
            lines.append(line)
    return lines

def main():
    if len(sys.argv) != 2:
        raise Exception('1 argument with file name expected')
    file_name = sys.argv[1]
    with open(file_name, 'r') as input_file:
        lines = split_long_lines(input_file)
    file_name_base, ext = os.path.splitext(file_name)
    res_file_name = file_name_base + '-split' + ext
    with open(res_file_name, 'w') as output_file:
        output_file.writelines(lines)

if __name__ == '__main__':
    main()