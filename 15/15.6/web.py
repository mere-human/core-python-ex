'''
15-6. Match simple Web domain names that begin with "www." and end with a ".com"
suffix, e.g., www.yahoo.com. Extra credit if your RE also supports other high-level
domain names: .edu, .net, etc., e.g., www.ucsc.edu.
'''

import re

def is_web_domain(text):
    m = re.match(r'www\.\w+\.(com|edu|net)', text)
    return (m is not None) and (m.group() == text)

assert is_web_domain('www.ucsc.edu')
assert is_web_domain('www.vk.com')
assert is_web_domain('www.wd40.net')
assert not is_web_domain('wd40.net')
assert not is_web_domain('wd40.nl')
assert not is_web_domain('-.nl')
