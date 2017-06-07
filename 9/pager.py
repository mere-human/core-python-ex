'''
9-4. File Access. Write a "pager" program. Your solution should prompt for a filename, and
display the text file 25 lines at a time, pausing each time to ask the user to "press a
key to continue.
'''
import sys
def main():
    file_name = sys.argv[0]
    f = open(file_name)
    lines = f.readlines()
    f.close()
    step = 10
    index = 0
    while True:
        if (index > len(lines)):
            break
        for line in lines[index:index+step]:
            print(line)
        index += step
        try:
            k = input('[Press a key to continue]')
        except (EOFError, KeyboardInterrupt) as e:
            print('Exit requested')
            break

if __name__ == '__main__':
    main()
