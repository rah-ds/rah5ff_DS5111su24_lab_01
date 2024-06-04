default:
	@cat makefile

#Download Raven only
get_raven_data:
	mkdir -p works
	wget -O works/raven.txt "https://www.gutenberg.org/cache/epub/17192/pg17192.txt"

raven_line_count raven.txt:
	cat raven.txt.txt | wc -l

raven_word_count raven.txt:
	cat raven.txt | wc -w

raven_counts raven.txt:
	echo "raven matches"
	cat raven.txt | grep "raven" | wc -l
	echo "Raven matches"
	cat raven.txt | grep "Raven" | wc -l
	echo "Raven or raven matches"
	cat raven.txt | grep -e "raven|Raven" | wc -l

get_texts:
	#already ran chmod 777
	python download_books.py

#Total all files -- including the raven
total_lines poems/:
	bat poems/*.txt | wc -l

total_words:
	bat poems/*.txt | wc -w
