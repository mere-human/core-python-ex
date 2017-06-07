'''
9-9. "PythonDoc." Go to the directory where your Python standard library modules are
located. Examine each .py file and determine whether a __doc__ string is available for
that module. If so, format it properly and catalog it. When your program has
completed, it should present a nice list of those modules that have documentation
strings and what they are. There should be a trailing list showing which modules do
not have documentation strings (the shame list). Extra credit: Extract documentation
for all classes and functions within the standard library modules.
'''

import os
import os.path

def read_1st_line(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        for line in f:
            if not line.lstrip().startswith('#') and not line.isspace():
                return line
    return None

def starts_with_string(line):
    if line[0] == 'r':
        return starts_with_string(line[1:])
    return line.startswith('"""') or line.startswith("'''")

def main():
    lib_dir = r'd:/Software/Python36-32/Lib'
    files_no_docs = []
    for entry in os.listdir(lib_dir):
        full_path = os.path.join(lib_dir, entry)
        if not os.path.isdir(full_path):
            line = read_1st_line(full_path)
            if not line or not starts_with_string(line):
                files_no_docs.append(entry)
    print('Files without doc strings:\n')
    print('\n'.join(files_no_docs))

if __name__ == '__main__':
    main()
