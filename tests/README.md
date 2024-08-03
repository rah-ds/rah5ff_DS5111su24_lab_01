## Testing

This project uses `pytest` for its parametrization, active community, and clear assertions.

## How to Run

```bash
python3 pytest tests

```
## Structure

```bash
├── README.md
├── functions
│   ├── test_clean_text.py
│   ├── test_count_words.py
│   └── test_tokenizer.py
└── test_utils.py
```

### Data Coverage

1) a line of English Text
2) A whole English Text
3) a sample of texts
4) French results


### Tested Functions
* `test_clean_text` - removes punctuation and returns a lowercase string.
* `test_count_words` - counts the words in a string.
* `test_tokenizer` - takes a string and returns a list.

### Misc Tests

#### utils
  * **test os** - only Mac, Windows, and Ubuntu supported
  
  * **python version** - only Python 3 supported
  
  * **written language compatibility** future support for Japanese, Chinese, and Korean
  
  * **Sanity checks** output vs stable and expected `wc` tool
