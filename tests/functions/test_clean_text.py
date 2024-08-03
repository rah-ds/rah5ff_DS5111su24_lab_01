import os
import sys
import pytest

sys.path.insert(0, os.path.abspath('src/'))
from tokenizer import clean_text, tokenizer
from utils import converts_book_to_string

def test_remove_punctuation():
    """
    GIVEN: a string of text
    WHEN: clean_text is run
    THEN: we shouldn't have commas or periods in the string
    """
    sample_text = ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that "
                   "one word he did outpour.")
    cleaned_string = clean_text(sample_text)

    assert "." not in cleaned_string, "the '.' character wasn't cleaned in the string"
    assert "," not in cleaned_string, "the "" character wasn't cleaned in the string"

@pytest.mark.parametrize("file_path", ["~rah5ff_DS5111su24_lab_01/works/testing_texts/The_Raven17192.txt"])
def test_on_file_remove_punctuation(file_path):
    print(file_path)



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


@pytest.mark.skip(reason="need to find some Edgar Allen Poe translations in Japanese/Chinese/Korean.")
def test_clean_text_japanese():
    """
    GIVEN: an input text from a popular multilingual language
    WHEN: we try and use our function
    THEN: we can expect the same functionality as if it was done in English / French
    """

    # use nltk - has functionality to check for chinese/japanese/korean characters
    # nltk.tokenize.util.is_cjk
    # python port of Moses tokenizer, An object that enumerates
    # the code points of the CJK characters as listed on
    # https://en.wikipedia.org/wiki/Basic_Multilingual_Plane # Basic_Multilingual_Plane

    # assert clean_text(cjk_text) == clean_text(text_english_french)
