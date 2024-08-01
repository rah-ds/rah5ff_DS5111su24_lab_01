import os
import sys

sys.path.insert(0, os.path.abspath("src/"))
from tokenize import clean_text #noqa


sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
cleaned_string = clean_text(sample_text)


def test_remove_punctuation(cleaned_string:str) -> None:
    """
    GIVEN: a string of text
    WHEN: clean_text is run
    THEN: we shouldn't have commas or periods in the string
    """
    assert "." not in cleaned_string, "the '.' character wasn't cleaned in the string"
    assert "," not in cleaned_string, "the "" character wasn't cleaned in the string"


def test_lower_string(cleaned_string) -> None:
    """
    GIVEN: a string of text
    WHEN: clean_text is run
    THEN:
    """
    assert cleaned_string.islower(), "the string isn't lowercase!"







