import os
import sys

sys.path.insert(0, os.path.abspath("src/"))
from tokenize import tokenizer, clean_text #noqa

sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
tokenizer_output = tokenizer(sample_text)

def test_tokenizer_output_is_list(tokenizer_output:list) -> None:
    """
    GIVEN: a tokenizer run
    WHEN: we run the tokenizer
    THEN: we get back a list
    """
    assert isinstance(tokenizer_output, list), "the tokenizer output isn't a list."

def test_tokenizer_split(tokenizer_output:list) -> None:
    """
    GIVEN: an input string
    WHEN: we split that string on whitespace
    THEN: we can expect its output to be list of certain size
    """

    assert len(tokenizer_output) == 25, "check the string split on whitespace" # should be a list of 25

def test_tokenizer_after_clean(tokenizer_output:list) -> None:
    """
    GIVEN: a string
    WHEN: we apply clean_text and tokenizer
    THEN: the output is the
    """
    assert True



print(clean_text(sample_text))
print(tokenizer(clean_text(sample_text)))