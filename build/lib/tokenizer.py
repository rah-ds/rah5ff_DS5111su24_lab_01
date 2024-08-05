"""
Taking an input text, this module cleans punctuations and counts the words.

Using Software Best Practices learned in DS_51111 - Data Engineering, this module
is the start of a rudimentary Text Analytics pipeline.
"""

from collections import Counter
import string
import sys


def clean_text(txt: str) -> str:
    """this takes a string and makes it lowercase and removes punctuations."""
    assert isinstance(txt, str), "the input must be a string"
    translation_tbl = str.maketrans('', '', string.punctuation)
    cleaned_text = txt.lower().translate(translation_tbl)
    assert isinstance(cleaned_text, str), "the output must be a string."
    return cleaned_text


def tokenizer(txt: str) -> list:
    """this takes a string and splits it into a list of words."""
    assert isinstance(txt, str), "the input must be a string"
    token_list = txt.split(" ")
    assert isinstance(token_list, list), "output must be a list."
    return token_list


def count_words(txt: str) -> dict:
    """Counts the words in a string, by cleaning the string
    and creating a frequency dictionary of the words."""
    assert isinstance(txt, str), "the input must be a string."
    count_dict = dict(Counter(tokenizer(clean_text(txt))))
    assert isinstance(count_dict, dict), "output must be a dictionary"
    return count_dict


if __name__ == "__main__":
    file_to_check = sys.argv[0]
    counts = count_words(file_to_check)

    print(f"cleaning and counting the words in this {file_to_check}")
    print(f"{counts}")
