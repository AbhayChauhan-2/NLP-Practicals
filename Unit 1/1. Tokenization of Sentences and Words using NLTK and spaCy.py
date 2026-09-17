
import nltk
import spacy

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing is interesting. It helps computers understand human language."

print("NLTK Tokenization")

sentences = nltk.sent_tokenize(text)
words = nltk.word_tokenize(text)

print("Sentences:")
print(sentences)

print("\nWords:")
print(words)


print("\nspaCy Tokenization")

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

print("Sentences:")
for sent in doc.sents:
    print(sent.text)

print("\nWords:")
for token in doc:
    print(token.text)