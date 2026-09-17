# Stop-word Removal using NLTK

import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is a simple example of stop word removal from a document."

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original Text:")
print(text)

print("\nAfter Stop-word Removal:")
print(filtered_words)