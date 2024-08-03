### Lab 1 Makefiles, Linux, Bash

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

# Lab 1 - Week 3
  * `clean_text` - should take a string, and should return all lowercase words, and throw out any punctuation
  * `tokenize` - should take a string and return a python list, where each item is a word in the file
  * `count_words` - should take a string and return a dictionary with the words as keys, and their counts as value

# Lab  Test Functions

Tests are written using a
* Given
* When
* Then
framework

we are going to limit what can change here
files under consideration:

> line count - name
* 17192 - `The Raven`
* 932 - `Fall of the House of Usher`
* 1063 - `Cask of Amontillado`
* 10031 - `The Poems`
* 14082 - `And Le Corbeau`