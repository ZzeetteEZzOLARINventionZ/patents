#!/bin/env python3

import os
import sys
import time

apply_dir = 'data/apply'
apply_fpath = 'meta/apply_files.txt'
apply_url_fmt = 'https://bulkdata.uspto.gov/data/patent/application/redbook/bibliographic/{}/{}'
overwrite = False

if not os.path.exists(apply_dir):
    os.makedirs(apply_dir)

url_list = []
for line in open(apply_fpath):
    line = line.strip()
    path = os.path.join(apply_dir, line)
    if not overwrite and os.path.isfile(path):
        continue

    if line.startswith('ipab'):
        year = line[4:8]
    elif line.startswith('pab'):
        year = line[3:7]
    else:
        print(f'{line}: not understood')
        sys.exit()

    url = apply_url_fmt.format(year, line)
    url_list.append((line, path, url))

for name, path, url in sorted(url_list):
    print(f'Fetching {name}')
    os.system(f'curl -o {path} {url}')
    print()
    time.sleep(10)

# to extract:
# cd data/apply
# ls | xargs -n 1 unzip
# rm *.txt
# rm *.html
