'''
9-22. ZIP Archive Files. The unzip -l command to dump the contents of ZIP archive is
boring. Create a Python script called lszip.py that gives additional information such
as: the compressed file size, the compressed percentage of each file (by comparing
the original and compressed file sizes), and a full time.ctime() timestamp instead of
the unzip output (of just the date and HH:MM). Hint: The date_time attribute of an
archived file does not contain enough information to feed to time.mktime()... it is up to
you!
'''

import zipfile
import sys
import time

def to_size_str(in_bytes):
    val = in_bytes
    units = ['B', 'KB', 'MB', 'GB']
    last_unit = None
    for u in units:
        last_unit = u
        if val < 1000:
            break
        val /= 1024
    return '{}{}'.format(round(val, 2), u)

def file_size(file_name):
    with open(file_name, 'rb') as f:
        return f.seek(0, 2) # seek to the end

def extract_zip_time(zip_info):
    l = []
    for i, x in enumerate(zip_info.date_time):
        if x < 10:
            l.append('0' + str(x)) # one-based to zero-based
        else:
            l.append(str(x))

    return time.strptime(' '.join(l), '%Y %m %d %H %M %S')

def main():
    if len(sys.argv) != 2:
        print('Single arg file name is expected')
        return
    file_name = sys.argv[1]
    if not zipfile.is_zipfile(file_name):
        print(file_name, 'is not a zip file')
        return
    fmt_str = '{} {} {} {} {} {}'
    with zipfile.ZipFile(file_name, 'r') as f:
        for name in f.namelist():
            inf = f.getinfo(name)
            t_struct = extract_zip_time(inf)
            secs = time.mktime(t_struct)
            t_str = time.ctime(secs)
            # print(dir(inf))
            # break
            if inf.is_dir():
                print(fmt_str.format('d', t_str, '\t', '\t', '\t', name))
            else:
                percents = round(inf.compress_size / inf.file_size * 100, 2) if inf.file_size else 0
                print(fmt_str.format('f', t_str, to_size_str(inf.file_size),
                      to_size_str(inf.compress_size), str(percents) + '%', name))
            # break

if __name__ == '__main__':
    main()