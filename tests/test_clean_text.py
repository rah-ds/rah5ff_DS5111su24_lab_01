import os
import sys

sys.path.insert(0, os.path.abspath('src/'))

from raven_tokenizer import clean_text, tokenizer

def test_remove_punctuation() -> None:
    """
    GIVEN: a string of text
    WHEN: clean_text is run
    THEN: we shouldn't have commas or periods in the string
    """
    sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    cleaned_string = clean_text(sample_text)

    assert "." not in cleaned_string, "the '.' character wasn't cleaned in the string"
    assert "," not in cleaned_string, "the "" character wasn't cleaned in the string"


def test_lower_string() -> None:
    """
    GIVEN: a string of text
    WHEN: clean_text is run
    THEN:
    """
    sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    cleaned_string = clean_text(sample_text)

    assert cleaned_string.islower(), "the string isn't lowercase!"







