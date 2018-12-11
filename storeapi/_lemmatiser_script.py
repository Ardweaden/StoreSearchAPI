import sys

sys.path.append("C:/Users/dis/Documents/JanJezersek/EkoSmart/pylemmagen")

from lemmagen.lemmatizer import Lemmatizer

a = Lemmatizer()

for i,word in enumerate(sys.argv):
	if i:
		sys.stdout.write(a.lemmatize(word) + " ")