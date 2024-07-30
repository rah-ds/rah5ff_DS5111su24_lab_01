default:
	@cat makefile

#Download Raven only
get_raven_data:
	mkdir -p works/
	wget -O works/raven.txt "https://www.gutenberg.org/cache/epub/17192/pg17192.txt"

#count lines in the rave
raven_line_count works/raven.txt:
	cat works/raven.txt | wc -l

#count words in the raven
raven_word_count:
	cat works/raven.txt | wc -w

#different counts of matches
raven_counts:
	echo "raven matches"
	cat works/raven.txt | grep "raven" | wc -w
	echo "Raven matches"
	cat works/raven.txt | grep "Raven" | wc -w
	echo "Raven or raven - matches"
	cat works/raven.txt | grep -E "raven|Raven" | wc -w

#get the other files
get_rest_of_texts:
	#already ran chmod 777, couldn't figure out bash script
	python download_other_books.py

#Total all files -- including the raven -- line counts
total_lines works/:
	bat works/*.txt | wc -l

#Total all works - word count
total_words:
	bat works/*.txt | wc -w

#clean up
clean_up:
	#delete the data if you'd like
	rm -rf works/

load_py_env:
	python3 -m venv tokenizer_env; pip install --upgrade pip; pip install -r requirements.txt