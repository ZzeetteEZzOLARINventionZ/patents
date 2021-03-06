#!/bin/env python3

import os
import time

assign_dir = 'data/assign'
assign_fname = 'meta/assign_files.txt'
assign_url_fmt = 'https://bulkdata.uspto.gov/data/patent/assignment/{}'
overwrite = False

if not os.path.exists(assign_dir):
    os.mkdir(assign_dir)

url_list = []
for line in open(assign_fname):
    line = line.strip()
    path = os.path.join(assign_dir, line)
    if not overwrite and os.path.isfile(path):
        continue

    year = int(line[2:6])

    url = assign_url_fmt.format(line)
    url_list.append((line, path, url))

for name, path, url in sorted(url_list):
    print(f'Fetching {name}')
    os.system(f'curl -o {path} {url}')
    print()
    time.sleep(1)

# extract files
# cd data/assign
# ls | xargs -n 1 unzip
