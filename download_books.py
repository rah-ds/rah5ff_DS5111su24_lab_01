#!usr/bin/python3

import os

book_ids = ["50852", "1063", "1064", "32037", "30092", "8893", "932", "15143", "51060", "10947"]

# create the directory
os.system(f"mkdir -p works/")

for id in book_ids:
    print(f"running {id}")
    os.system(f'wget -O "works/{id}.txt "https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"')
