import os
import subprocess
import sys
import pytest
import platform

import tempfile

sys.path.insert(0, os.path.abspath('src/'))

from raven_tokenizer import clean_text, tokenizer, count_words


def test_platform_compatibility():
    """
    GIVEN: a test suite
    WHEN: this library is called
    THEN: fail on unsupported platforms

    currently only Windows, Ubuntu, and Mac are supported.
    """
    supported_os_ = ["windows", "macos", "ubuntu"]
    current_os = clean_text(platform.platform())

    assert current_os in supported_os_, f"given os {current_os} only {supported_os_} supported"


def test_python_version():
    """
    GIVEN: a test suite
    WHEN: this library is committed
    THEN: make sure the Python Version is 3

    only Python 3 is currently actively supported.
    """
    assert sys.version_info.major == 3, \
        f"only Python 3 is supported! currently calling {sys.version}"


@pytest.mark.skip(reason="need to find some Edgar Allan Poe translations in"
                         " Japanese/Chinese/Korean.")
def test_clean_text_japanese():
    """
    GIVEN: an input text from a popular multilingual language
    WHEN: we try and use our clean text function
    THEN: we can expect the same functionality as if it was done in English / French
    """

    # use nltk - has functionality to check for chinese/japanese/korean characters
    # nltk.tokenize.util.is_cjk
    # python port of Moses tokenizer, An object that enumerates
    # the code points of the CJK characters as listed on
    # https://en.wikipedia.org/wiki/Basic_Multilingual_Plane # Basic_Multilingual_Plane

    # assert clean_text(cjk_text) == clean_text(text_english_french)


def test_wc_vs_counter():
    """
    GIVEN: our tokenizer
    WHEN: we compare it vs word counter
    THEN: are the two giving the same answer.

    wc has a lot of support, and our tokenizer should
    give the same answer as this benchmark.
    """
    # with tempfile.NamedTemporaryFile()
    # subprocess.check_output(["wc" "-w", "file"])
    # os.sys(f"echo ${sample_text} | wc -w")
    # echo
    # "$tsetat adaf adfa " | wc - w
