#!usr/bin/python3

import os

book_ids_d = {"Bells_and_Poems": 50852,
              "Cask_of_Amontillado": 1063,
              "Masque_of_the_Red_Death": 1064,
              "Eureka_Poems": 32037,
              "Lords_of_the_Housetops": 30092,
              "Selections_from_Poe": 8893,
              "The_Fall_of_the_House_of_Usher": 932,
              "Famous_Modern_Ghost_Stories": 15143,
              "Arthur_Gordon_Pym": 51060,
              "Best_American_Humorous_Short_Stories": 10947
              }

# create the directory
os.system(f"mkdir -p works/")

for book_name, book_id in book_ids_d.items():
    print(f"running {book_name} - {book_id}")
    os.system(f'wget -O "works/{book_name}_{book_id}.txt" "https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"')
