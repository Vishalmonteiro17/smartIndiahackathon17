import nltk as nlp
import time
#c_proc.terminate()
while(1):
	f = open("a.txt",'r')
	data = f.read()
	words = nlp.word_tokenize(data)
	tagged = nlp.pos_tag(words)
	print(tagged)	
	f.close()
	time.sleep(10)

