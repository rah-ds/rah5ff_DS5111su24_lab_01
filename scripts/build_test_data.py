#!usr/bin/python3
"""
build the data needed for testing.

output is a json file for each of the tests that can be imported into the
pytest suite.
"""

import os
import json
import sys


os.chdir("..")  # stored in scripts needs to be run in root
sys.path.insert(0, os.path.abspath('src/'))
from utils import converts_book_to_string


test_d = {"The_Raven_Text": converts_book_to_string("data/raw/The_Raven_17192.txt"), "English_Poe_Text": ",".join(
    [converts_book_to_string((os.path.join("data/raw", file))) for file in [
        "The_Raven_17192.txt",
        "Cask_of_Amontillado_1063.txt",
        "Fall_of_the_House_of_Usher_932.txt",
        "The_Poems_10031.txt"]]),
          "French_Poe_Text": converts_book_to_string("data/raw/Le_Corbeau_14082.txt")}

with open("tests/tokenizer/books_as_strings.json", "w") as json_file:
    json.dump(test_d, json_file, indent=4)
