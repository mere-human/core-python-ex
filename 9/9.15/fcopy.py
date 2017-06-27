'''
9-15. Copying Files. Prompt for two filenames (or better yet, use command-line arguments).
The contents of the first file should be copied to the second file.
'''
import sys

def main():
    if len(sys.argv) != 3:
        raise ArgumentError('Expected 2 args with file names')
    src_file_name, dst_file_name = sys.argv[1:]
    print('Copy', src_file_name, 'into', dst_file_name)
    with open(src_file_name, 'r') as src_file,\
         open(dst_file_name, 'w') as dst_file:
        for line in src_file:
            dst_file.write(line)
    print('Done!')

if __name__ == '__main__':
    main()
