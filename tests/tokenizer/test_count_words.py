import os
import pytest
import sys
import json

sys.path.insert(0, os.path.abspath('src/'))
from tokenizer import count_words

test_data = json.load(open("tests/tokenizer/books_as_strings.json"))


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

    assert "Raven" not in count_dict, "we shouldn't see an upper case character in this in output"


@pytest.mark.parametrize("data_key", ["The_Raven_Text", "English_Poe_Text", "French_Poe_Text"])
def test_no_extra_words(data_key: str):
    """
    GIVEN: we run the function count words
    WHEN: we run the sample text
    THEN: we don't have original names in the output test.
    """

    count_dict = count_words(test_data[data_key])

    assert "Raven" not in count_dict, "we shouldn't see an upper case character in this in output"



def test_wc_vs_counter(raven_poem:str = test_data["The_Raven_Text"]):
    """
    GIVEN: our tokenizer
    WHEN: we compare the count vs. word counter
    THEN: are the two giving the same answer.

    wc has a lot of support, and our tokenizer should
    give the same answer as this benchmark.
    """

    # from word counter for the Raven - 10,231 words
    counter_output = count_words(raven_poem)
    total_words = sum(counter_output.values())

    assert total_words > 100231, f"total words {total_words}  should be greater than counter as we clean text"