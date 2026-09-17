# Parsing and Chunking using RegEx and spaCy

import spacy

nlp = spacy.load("en_core_web_sm")

text = "The young boy is playing football in the park."

doc = nlp(text)

print("Tokens:")
for token in doc:
    print(token.text, "->", token.pos_)

# Chunking
print("\nNoun Phrases:")

for chunk in doc.noun_chunks:
    print(chunk.text)

# Dependency Parsing
print("\nDependency Parsing:")

for token in doc:
    print(token.text, "->", token.dep_, "->", token.head.text)

import nltk

sentence = "The young boy plays football."

words = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN>}"

chunk_parser = nltk.RegexpParser(grammar)

tree = chunk_parser.parse(tags)

print(tree)
tree.pretty_print()