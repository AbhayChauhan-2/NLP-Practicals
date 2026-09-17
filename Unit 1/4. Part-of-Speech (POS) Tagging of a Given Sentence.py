# POS Tagging using NLTK

import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

sentence = "The quick brown fox jumps over the lazy dog."

words = word_tokenize(sentence)

tags = pos_tag(words)

print("POS Tags:")

for word, tag in tags:
    print(word, "->", tag)