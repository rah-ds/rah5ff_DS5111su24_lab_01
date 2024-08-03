import os
import sys
import pytest

sys.path.insert(0, os.path.abspath('src/'))

from raven_tokenizer import clean_text, tokenizer, count_words


def test_tokenizer_output_is_list():
    """
    GIVEN: the tokenizer function
    WHEN: we run the tokenizer
    THEN: the return data should be a list
    """
    sample_text = ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that "
                   "one word he did outpour.")

    tokenizer_output_ = tokenizer(sample_text)
    assert isinstance(tokenizer_output_, list), "the tokenizer output isn't a list."

    tokenizer_output_ = tokenizer(clean_text(sample_text))  # worth checking this after the clean_text function as well
    assert isinstance(tokenizer_output_, list), "the tokenizer output after cleaning isn't a list."


def test_tokenizer_split():
    """
    GIVEN: an input string
    WHEN: we split that string on whitespace
    THEN: we can expect its output to be list of certain size
    """
    sample_text = ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that "
                   "one word he did outpour.")
    tokenizer_output_ = tokenizer(sample_text)

    assert len(tokenizer_output_) == 25, "check the string split on whitespace"  # should be a list of 25 from sample
    # input

    tokenizer_output_ = tokenizer(clean_text(sample_text))
    assert len(
        tokenizer_output_) == 25, "check the string split on whitespace after clean"  # should be a list of 25 from
    # sample input


@pytest.mark.xfail(reason="the input must be a string.")
def test_input_cant_be_a_string():
    """
    GIVEN: an input that isn't a string
    WHEN: the clean_function is run
    THEN: an assertion error should stop the function
    """
    not_string_input_ = [99999, 9.8898, [], None]
    with pytest.raises(AssertionError):
        for should_fail in not_string_input_:
            clean_text(should_fail)

















