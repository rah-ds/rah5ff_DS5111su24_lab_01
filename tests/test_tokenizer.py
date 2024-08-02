import os
import sys

sys.path.insert(0, os.path.abspath('src/'))
from raven_tokenizer import count_words

# def count_words(txt: str) -> dict:
#     """Counts the words in a string, by cleaning the string
#     and creating a frequency dictionary of the words."""
#     assert isinstance(txt, str), "the input must be a string."
#     count_dict = dict(Counter(tokenizer(clean_text(txt))))
#     assert isinstance(count_dict, dict), "output must be a dictionary"
#     return count_dict

def test_count_words() -> None:
    """
    GIVEN: count words
    WHEN: we run the sample text
    THEN: we should be able to expect the counts
    """
    sample_text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    count_dict = count_words(sample_text)

    assert count_dict["the"] == 2, "the should appear twice"
def test_count_words_dtype() -> None:
    """
    GIVEN:
    WHEN:
    THEN:
    """

def test_count_words() -> None:
    """
    GIVEN:
    WHEN:
    THEN:
    """
