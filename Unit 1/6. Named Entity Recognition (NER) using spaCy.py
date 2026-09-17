# Named Entity Recognition using spaCy

import spacy

nlp = spacy.load("en_core_web_sm")

text = """
Abhay is studying Computer Science at NIET in Greater Noida.
He wants to work at Google in the future.
"""

doc = nlp(text)

print("Named Entities:")

for entity in doc.ents:
    print(entity.text, "->", entity.label_)