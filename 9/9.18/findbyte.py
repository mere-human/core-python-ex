'''
9-18. Searching Files. Obtain a byte value (0-255) and a filename. Display the number of
times that byte appears in the file.
'''

import sys

def main():
    if len(sys.argv) != 3:
        raise Exception('2 arguments for file name and byte value (0-255) are expected')
    file_name = sys.argv[1]
    byte_val = int(sys.argv[2])
    if byte_val < 0 or byte_val > 255:
        raise ValueError('Value %d is out of expected range 0-255' % byte_val)
    n_bytes = 0
    with open(file_name, 'rb') as input_file:
        while True:
            input_byte = input_file.read(1)
            if not input_byte:
                break
            if input_byte[0] == byte_val:
                n_bytes += 1

    print('Found %d occurences' % n_bytes)
if __name__ == '__main__':
    main()