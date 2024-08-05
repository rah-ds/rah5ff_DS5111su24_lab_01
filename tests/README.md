## Testing

This project uses `pytest` for its parametrization, active community, and clear assertions.

## How to Run

```bash
#from project root
python3 pytest tests --verbose

```

## Data Coverage

1) Sample line of English Text
2) The text of the Raven
3) English Sample of Edgar Allan Poe Texts
4) French Sample from `Le Corbeau`
## Structure

```bash
├── README.md
├── functions
│   ├── test_clean_text.py
│   ├── test_count_words.py
│   └── test_tokenizer.py
└── test_utils.py
```

### Functions
* `test_clean_text` - removes punctuation and returns a lowercase string.
* `test_count_words` - counts the words in a string.
* `test_tokenizer` - takes a string and returns a list.

### Other Tests

#### Platform
  * **test os** - only Mac, Windows, and Ubuntu supported
  
  * **python version** - only Python 3 supported
  
  * **written language compatibility** future support for Japanese, Chinese, and Korean
  
  * **Sanity checks** output vs stable and expected `wc` tool

#### Integration Tests

