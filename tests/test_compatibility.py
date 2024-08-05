import os
import pytest
import platform
import sys

sys.path.insert(0, os.path.abspath('src/'))


# from tokenizer import clean_text, tokenizer, count_words


def test_platform_compatibility():
    """
    GIVEN: a test suite
    WHEN: this library is called
    THEN: fail on unsupported platforms

    currently only Windows, Ubuntu, and Mac are supported.
    """
    supported_os_ = ["Windows", "Darwin", "Ubuntu", "Linux"]
    current_os = platform.system()

    assert current_os in supported_os_, f"given os {current_os} only {supported_os_} supported"


def test_python_version():
    """
    GIVEN: a test suite
    WHEN: this library is committed
    THEN: make sure the Python Version is 3.6+

    only Python 3 is currently actively supported.
    """
    assert ((sys.version_info.major == 3) and (sys.version_info.minor > 6)), \
        f"only Python 3.6+ is supported! currently calling {sys.version}"


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


def test_pytest_version():
    """GIVEN: a call to pytest and build
       WHEN: we run pytest
       THEN: check if the version is the one in the requirements.txt"""

    assert pytest.__version__ == '8.3.2', f"pytest {pytest.__version__}  -- expected 8.3.2"
