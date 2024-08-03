import os
import pytest
import sys

sys.path.insert(0, os.path.abspath('src/'))
from tokenizer import count_words


def test_count_words_count():
    """
    GIVEN: count words
    WHEN: we run the sample text
    THEN: we should be able to expect the counts
    """
    sample_text = ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that "
                   "one word he did outpour.")
    count_dict = count_words(sample_text)

    assert (count_dict["the"] == 2), "'the' should appear twice, from the sample input"
    assert (count_dict["outpour"] == 1), "outpour should a appear once in the sample and without punctuation."


def test_no_extra_words():
    """
    GIVEN: count words
    WHEN: we run the sample text
    THEN: we don't have original names in the output test.
    """
    sample_text = ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that "
                   "one word he did outpour.")
    count_dict = count_words(sample_text)

    assert "Raven" not in count_dict, "we shouldn't see an upper case and in this in output"

# def check