default:
	@cat makefile

download_books:
	cd scripts && python3 download_other_books.py && python3 build_test_data.py;

env:
	python3 -m venv env; source env/bin/activate ; pip install --upgrade pip

update: env
	source env/bin/activate; pip install -r requirements.txt

lint:
	pylint --generate-rcfile >> pylintrc; pylint src/ > pylint_out.txt

tests: lint # only non integration tests
	pytest -vvx tests/ -m "not integration"


#all: download_books, env, update, lint, tests

clean_up: download_books
	rm -rf tests/tokenizer/books_as_strings.json
	rm -rf data


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
