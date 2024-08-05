import os
import sys
import pytest
import json

sys.path.insert(0, os.path.abspath('src/'))
from tokenizer import clean_text, tokenizer, count_words

test_data = json.load(open("tests/tokenizer/books_as_strings.json"))


@pytest.mark.integration
@pytest.mark.parametrize("data_key", ["The_Raven_Text", "English_Poe_Text", "French_Poe_Text"])
def test_tokenizer_pipelines(data_key: str):
    """
    GIVEN: count calls clean text and tokenizer
    WHEN: we compare the output of calling all separately
    THEN: they should give the same results
    """
    data = test_data[data_key]

    pipeline_one = clean_text(data)
    pipeline_one = tokenizer(pipeline_one)
    pipeline_one = count_words(" ".join(pipeline_one))

    pipeline_two = count_words(data)

    assert pipeline_one == pipeline_two, "count function integrates properly."


@pytest.mark.integration
@pytest.mark.parametrize("data_key", ["The_Raven_Text", "English_Poe_Text", "French_Poe_Text"])
def test_count_works(data_key: str):
    """
    GIVEN: count_words returns most_common first
    WHEN: we count words in a whole text
    THEN: the counts should be over a baseline amount

    This is a check that the first key of count words makes sense

    """

    test_data = json.load(open("tests/tokenizer/books_as_strings.json"))

    data = count_words(test_data[data_key])
    most_common_word = list(data.keys())[0]  # should be sorted

    assert data.get(most_common_word) > 100, "tokenizer results seem low for whole text"
