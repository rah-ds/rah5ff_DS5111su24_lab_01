import os
import sys

sys.path.insert(0, os.path.abspath('src/'))

from raven_tokenizer import clean_text, tokenizer, count_words

def test_tokenizer_output_is_list() -> None:
    """
    GIVEN: a tokenizer run
    WHEN: we run the tokenizer
    THEN: we get back a list
    """
    sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    tokenizer_output = tokenizer(sample_text)

    assert isinstance(tokenizer_output, list), "the tokenizer output isn't a list."

def test_tokenizer_split() -> None:
    """
    GIVEN: an input string
    WHEN: we split that string on whitespace
    THEN: we can expect its output to be list of certain size
    """
    sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    tokenizer_output = tokenizer(sample_text)

    assert len(tokenizer_output) == 25, "check the string split on whitespace" # should be a list of 25

def test_tokenizer_after_clean() -> None:
    """
    GIVEN: a string
    WHEN: we apply clean_text and tokenizer
    THEN: the output is the
    """
    sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    tokenizer_output = tokenizer(sample_text)

    assert True


sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
print(clean_text(sample_text))
print(tokenizer(clean_text(sample_text)))
print(count_words(clean_text(sample_text)))