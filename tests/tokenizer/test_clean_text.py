import os
import sys
import pytest
import json

sys.path.insert(0, os.path.abspath('src/'))
from tokenizer import clean_text, tokenizer

test_data = json.load(open("tests/tokenizer/books_as_strings.json"))


def test_remove_punctuation_simple():
    """
    GIVEN: a string of text
    WHEN: clean_text is run
    THEN: we shouldn't have commas or periods in the string
    """
    sample_text = ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that "
                   "one word he did outpour.")
    cleaned_string = clean_text(sample_text)

    assert "." not in cleaned_string, "the '.' character wasn't cleaned in the string"
    assert "," not in cleaned_string, "the , character wasn't cleaned in the string"


@pytest.mark.parametrize("data_key", ["The_Raven_Text", "English_Poe_Text", "French_Poe_Text"])
def test_remove_punctuation_on_books(data_key):
    """
    GIVEN: a range of texts
    WHEN: clean_text is run
    THEN: there are no commas or periods in the text
    """

    cleaned_string = clean_text(test_data[data_key])
    assert "." not in cleaned_string, "the . character exists in the string"
    assert "," not in cleaned_string, "the , character exists in the string"


def test_lower_string():
    """
    GIVEN: a string of text
    WHEN: clean_text is run
    THEN: we should have the string be lowercase.
    """
    sample_text = ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that "
                   "one word he did outpour.")
    cleaned_string = clean_text(sample_text)

    assert cleaned_string.islower(), "the string isn't lowercase!"


@pytest.mark.parametrize("data_key", ["The_Raven_Text", "English_Poe_Text", "French_Poe_Text"])
def test_lower_string_on_books(data_key):
    """
    GIVEN: a string of text
    WHEN: clean_text is run
    THEN: we should have the string be lowercase.
    """
    cleaned_string = clean_text(test_data[data_key])

    assert cleaned_string.islower(), "the string isn't lowercase!"


@pytest.mark.xfail(reason="the input isn't a string.")
def test_input_is_not_a_string():
    """
    GIVEN: an input that isn't a string
    WHEN: the tokenizer is run
    THEN: an assertion error should stop the function
    """
    not_string_input_ = [99999, 9.8898, [], None, True, {}, 0, 0.00]
    with pytest.raises(AssertionError):
        for should_fail in not_string_input_:
            clean_text(should_fail)
