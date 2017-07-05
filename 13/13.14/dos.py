'''
13-14. DOS. Write a Unix interface shell for DOS machines. You present the user a command
line where he or she can type in Unix commands, and you interpret them and output
accordingly, i.e., the "ls" command calls "dir" to give a list of filenames in a directory,
"more" uses the same command (paginating through a text file), "cat" calls "type,"
"cp" calls "copy," "mv" calls "ren," and "rm" invokes "del," etc.
'''

import os

def main():
    cmd_dict = {
        'ls':'dir',
        'more':'more',
        'cat':'type',
        'cp':'copy',
        'mv':'ren',
        'rm':'del'
    }
    while True:
        input_str = input('$ ')
        if input_str == 'pwd':
            print(os.getcwd())
            continue
        pos = input_str.find(' ')
        if pos > 0:
            cmd = input_str[:pos] 
            args = input_str[pos:]
        else:
            cmd = input_str
            args = ''
        dos_cmd = cmd_dict.get(cmd)
        if dos_cmd:
            os.system(dos_cmd + args)
        else:
            print('Unknown command')
            break

if __name__ == '__main__':
    main()