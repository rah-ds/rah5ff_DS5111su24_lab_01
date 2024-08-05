## Lab 1 
[![Python package](https://github.com/rah-ds/rah5ff_DS5111su24_lab_01/actions/workflows/validations.yml/badge.svg)](https://github.com/rah-ds/rah5ff_DS5111su24_lab_01/actions/workflows/validations.yml)
Developing a well-tested and robust tokenizer library. 

A quick start demo can be found in `demo\demos.ipynb`


<!-- TOC -->
  * [Lab 1](#lab-1-)
    * [Week 1—Makefiles, Linux, Bash](#week-1makefiles-linux-bash)
        * [The 10 works we run are:](#the-10-works-we-run-are)
    * [Week 3—Defining Functions](#week-3defining-functions)
    * [Week 4—Testing Functions](#week-4testing-functions)
<!-- TOC -->


### Week 1—Makefiles, Linux, Bash

This lab uses project [Gutenburg](https://www.gutenberg.org/ebooks/1065)
to load and analyze books/works that no longer have Copyrights. 

Being at UVa, we naturally care about Edgar Allan Poe :).

To download and analyze some of his works, we will use a makefile, which runs on:
1) The famous `Raven` Poem
2) On his `total` works which is the `Raven` and another 10 works selected.

##### The 10 works we run are:

  * [The Bells and other Poems](https://gutenberg.org/cache/epub/50852/pg50852.txt)
  * [The Cask of Amontillado](https://gutenberg.org/cache/epub/1063/pg1063.txt)
  * [The Masque of the Red Death](https://gutenberg.org/cache/epub/1064/pg1064.txt)
  * [Eureka: A Prose Poem](https://gutenberg.org/cache/epub/32037/pg32037.txt)
  * [Lords of the Housetops: Thirteen Cat Tales](https://gutenberg.org/cache/epub/30092/pg30092.txt)
  * [Selections from Poe](https://gutenberg.org/cache/epub/8893/pg8893.txt)
  * [The Fall of the House of Usher](https://gutenberg.org/cache/epub/932/pg932.txt)
  * [Famous Modern Ghost Stories](https://gutenberg.org/cache/epub/15143/pg15143.txt)
  * [The Narrative of Arthur Gordon Pym of Nantucket](https://gutenberg.org/cache/epub/51060/pg51060.txt)
  * [The Best American Humorous Short Stories](https://gutenberg.org/cache/epub/10947/pg10947.txt)

I think some of these might contain the `The Raven` Poem but, I got what I could!

The make file is self documenting and calling
```shell
make 
```
will echo the make file.

the argument calls to `make` are 
* `get_raven_data`
* `raven_line_count`
* `raven_word_count`
* `raven_counts`
* `get_rest_of_texts`
* `total_lines`
* `total_words`
* `clean_up`

### Week 3—Defining Functions

  * `clean_text` - should take a string, and should return all lowercase words, and throw out any punctuation
  * `tokenize` - should take a string and return a python list, where each item is a word in the file
  * `count_words` - should take a string and return a dictionary with the words as keys, and their counts as value

### Week 4—Testing Functions

Tests are written using a Gherkin (Given/When/Then) Scenario Framework

* Given (a setup - data and preconditions)
* When (an action or scenario happens)
* Then (a result or outcome)


we are going to limit what can change here
files under consideration:


| Book Title                 | Project Gutenberg ID |
|----------------------------|----------------------|
| The Raven                  | 17192                |
| Fall of the House of Usher | 932                  |
| Cask of Amontillado        | 1063                 |
| The Poems                  | 10031                |
| Le Corbeau                 | 14082                |

### Week 5 GitHub Actions

