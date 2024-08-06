default:
	@cat makefile

env:
	python3 -m venv env; source env/bin/activate ; pip install --upgrade pip

update: env
	source env/bin/activate; pip install -r requirements.txt

download_books:
	cd scripts && python3 download_other_books.py && python3 build_test_data.py;

.PHONY: lint
lint:
	pylint src/tokenizer.py

.PHONY: tests
tests: update # only non integration tests
	source env/bin/activate; pytest -vvx tests/ -m "not integration"

.PHONY: clean_up
clean_up:
	rm -rf tests/tokenizer/books_as_strings.json
	rm -rf data

.PHONY: all
make all:
	make env
	make update
	make download_books
	make lint
	make tests
	make clean_up

.PHONY: install_from_github
make install_from_github: env
	 pip install git+https://github.com/rah-ds/rah5ff_DS5111su24_lab_01.git

##########################
####################################
############### EXPLORING TEXTS @@
#########################################

##Download Raven only
#get_raven_data:
#	mkdir -p data/raw/
#	wget -O data/raw/The_Raven_17192.txt "https://www.gutenberg.org/cache/epub/17192/pg17192.txt"
#
##count lines in the raven file
#raven_line_count data/raw/The_Raven_17192.txt:
#	cat data/raw/The_Raven_17192.txt | wc -l
#
##count words in the raven
#raven_word_count:
#	cat data/raw/The_Raven_17192.txt | wc -w
#
##different counts of matches
#raven_counts:
#	echo "raven matches"
#	cat data/raw/The_Raven_17192.txt | grep "raven" | wc -w
#	echo "Raven matches"
#	cat data/raw/The_Raven_17192.txt | grep "Raven" | wc -w
#	echo "Raven or raven - matches"
#	cat data/raw/The_Raven_17192.txt | grep -E "raven|Raven" | wc -w
#
###get the other files
#get_rest_of_texts: data/raw/The_Raven_17192.txt
#	python3 scripts/download_other_books.py
#
##Total all files -- including the raven -- line counts
#total_lines data/raw/:
#	bat data/raw/*.txt | wc -l
#
##Total all data - word count
#total_words:
#	bat data/raw/*.txt | wc -w
