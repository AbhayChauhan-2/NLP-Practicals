
import nltk
import spacy

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = "The students are studying studies and playing games."

words = nltk.word_tokenize(text)

stemmer = PorterStemmer()

print("Stemming:")
for word in words:
    print(word, "->", stemmer.stem(word))


lemmatizer = WordNetLemmatizer()

print("\nLemmatization:")
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))