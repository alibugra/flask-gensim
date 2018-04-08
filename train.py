from gensim.models import Word2Vec
import nltk

file = open("data/sentences.txt", 'r', encoding='utf8')
sentences = []
for line in file:
    line = line.lower()
    words = nltk.word_tokenize(line)
    words = [word.lower() for word in words if word.isalpha()]
    sentences.append(words)

model = Word2Vec(sentences, min_count=1)

model.save("model/trained_model.bin")
