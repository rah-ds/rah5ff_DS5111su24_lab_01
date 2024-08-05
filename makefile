default:
	@cat makefile


download_books:
	cd scripts && python3 download_other_books.py && python3 build_test_data.py;

env:
	python3 -m venv env; source env/bin/activate ; pip install --upgrade pip

update: env
	source env/bin/activate; pip install -r requirements.txt

lint: update, download_books
	pylint src/tokenizer.py

tests: lint, download_books
	pytest -vvx tests/

clean_up: download_books
	rm -rf tests/tokenizer/books_as_strings.json
	rm -rf data/


##########################
####################################
############### EXPLORING TEXTS @@
#########################################

##Download Raven only
get_raven_data:
	mkdir -p data/
	wget -O data/raven.txt "https://www.gutenberg.org/cache/epub/17192/pg17192.txt"

#count lines in the raven file
raven_line_count data/raven.txt:
	cat data/raven.txt | wc -l

#count words in the raven
raven_word_count:
	cat data/raven.txt | wc -w

#different counts of matches
raven_counts:
	echo "raven matches"
	cat data/raven.txt | grep "raven" | wc -w
	echo "Raven matches"
	cat data/raven.txt | grep "Raven" | wc -w
	echo "Raven or raven - matches"
	cat data/raven.txt | grep -E "raven|Raven" | wc -w

##get the other files
get_rest_of_texts: data/raven.txt
	python3 scripts/download_other_books.py

#Total all files -- including the raven -- line counts
total_lines data/:
	bat data/*.txt | wc -l

#Total all data - word count
total_words:
	bat data/*.txt | wc -w
