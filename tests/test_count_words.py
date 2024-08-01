import os
import sys

sys.path.insert(0, os.path.abspath("src/"))
from tokenize import token#noqa

sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
cleaned_string = clean_text(sample_text)


def tokenizer(txt: str) -> list:
    """this takes a string and splits it into a list of words."""
    assert isinstance(txt, str), "the input must be a string"
    token_list = txt.split(" ")
    assert isinstance(token_list, list), "output must be a list."
    return token_list


def test_tokenizer(cleaned_string:str) -> None:
