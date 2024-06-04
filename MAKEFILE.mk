default:
	cat @make 

get_texts:

#Raven only
get__raven_data:
	wget -O https://www.gutenberg.org/cache/epub/17192/pg17192.txtLinks to an external site.

raven_line_count:
	wc -l

raven_word_count:
	grep raven.csv |

#Total all files
total_lines:


total_words:

