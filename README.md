
![Supported Versions](https://img.shields.io/badge/python_version-3.8%7C3.9%7C3.10%7C3.11%7C3.12-blue.svg)
[![Python package](https://github.com/rah-ds/rah5ff_DS5111su24_lab_01/actions/workflows/validations.yml/badge.svg)](https://github.com/rah-ds/rah5ff_DS5111su24_lab_01/actions/workflows/validations.yml)


## Lab 1 

Developing a well-tested and robust tokenizer library. 

A quick start demo can be found in `demo\demos.ipynb`

To learn how the tests are run check out the [tests/readme](tests/README.md)

<details open> 
<summary> Development Process </summary>

<!-- TOC -->
  * [Lab 1](#lab-1-)
    * [Week 1—Makefiles, Linux, Bash](#week-1makefiles-linux-bash)
        * [Initially Considered Set](#initially-considered-set)
    * [Week 3—Defining Functions](#week-3defining-functions)
    * [Week 4—Testing Functions](#week-4testing-functions)
    * [Week 5-GitHub Actions](#week-5-github-actions)
    * [Week 6-Installable Package](#week-6-installable-package)
    * [Week 7-Review](#week-7-review)
    * [Week 8-Refactoring and Linting](#week-8-refactoring-and-linting)
<!-- TOC -->


### Week 1—Makefiles, Linux, Bash

This lab uses project [Gutenberg](https://www.gutenberg.org/ebooks/1065)
to load and analyze books/works that no longer have Copyrights. 

Being Students at UVa, we naturally care about Edgar Allan Poe.

To download and analyze some of his works, we will use a makefile, which runs on:
1) The famous `Raven` Poem
2) On his `total` works which is the `Raven` and another 10 works selected.

##### Initially Considered Set

The 10 works we run are:

| Considered Number | Gutenberg Text Link                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------------|
| 1                 | [The Bells and other Poems](https://gutenberg.org/cache/epub/50852/pg50852.txt)                       |
| 2                 | [The Cask of Amontillado](https://gutenberg.org/cache/epub/1063/pg1063.txt)                           |
| 3                 | [The Masque of the Red Death](https://gutenberg.org/cache/epub/1064/pg1064.txt)                       |
| 4                 | [Eureka: A Prose Poem](https://gutenberg.org/cache/epub/32037/pg32037.txt)                            |
| 5                 | [Lords of the Housetops: Thirteen Cat Tales](https://gutenberg.org/cache/epub/30092/pg30092.txt)      |
| 6                 | [Selections from Poe](https://gutenberg.org/cache/epub/8893/pg8893.txt)                               |
| 7                 | [The Fall of the House of Usher](https://gutenberg.org/cache/epub/932/pg932.txt)                      |
| 8                 | [Famous Modern Ghost Stories](https://gutenberg.org/cache/epub/15143/pg15143.txt)                     |
| 9                 | [The Narrative of Arthur Gordon Pym of Nantucket](https://gutenberg.org/cache/epub/51060/pg51060.txt) |
| 10                | [The Best American Humorous Short Stories](https://gutenberg.org/cache/epub/10947/pg10947.txt)        |



I think some of these might contain the `The Raven` Poem but, I got what I could!

The make file is self documenting and calling
```shell
make 
```
will echo the make file and show everything available.

some argument calls to `make` to explore the texts could be
* `get_raven_data`
  * `raven_line_count`
  * `raven_word_count`
  * `raven_counts`
* `get_rest_of_texts`
  * `total_lines`
  * `total_words`

uncomment them in the file first the rest of the calls will be focused on building the pipeline.
 
   
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

### Week 5-GitHub Actions
* Workflow Automation: launching and automated workflow and
adding some Integration tests
* updated requirements.txt to be a specific version

### Week 6-Installable Package
* built out the pyproject.toml file, could've also used a setup.py file
* updated the Demo to include a user-friendly way to call package

### Week 7-Review
* review - focused on what we learned and writing some more tests

### Week 8-Refactoring and Linting
* refactored until there was an acceptable score (10/10) in Pylint
</details>
