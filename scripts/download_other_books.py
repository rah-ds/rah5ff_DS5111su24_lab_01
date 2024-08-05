#!usr/bin/python3

import os

# books we are interested in
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

# keeping a constant suite of baseline books for testing
testing_book_ids_d = {
    "The_Raven": 17192,
    "Fall_of_the_House_of_Usher": 932,
    "Cask_of_Amontillado": 1063,
    "The_Poems": 10031,
    "Le_Corbeau": 14082
}


# os.system(f"mkdir -p works/build_texts")
#
# for book_name, book_id in book_ids_d.items():
#     print(f"running {book_name} - {book_id}")
#     os.system(
#         f'wget -O "works/{book_name}_{book_id}.txt" "https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"')

os.system(f"mkdir -p ..//data/raw/")

for book_name, book_id in testing_book_ids_d.items():
    print(f"running {book_name} - {book_id}")
    os.system(
        f'wget -O "..//data/raw/{book_name}_{book_id}.txt" "https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"')
