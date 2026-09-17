# NLP Unit 1 Practicals

This repository contains **Unit 1 Natural Language Processing (NLP) practical programs** implemented in Python using **NLTK** and **spaCy**.

The practicals cover fundamental NLP preprocessing and linguistic analysis techniques such as tokenization, stemming, lemmatization, stop-word removal, POS tagging, parsing, chunking, and Named Entity Recognition.

## 📚 Practicals Included

| S. No. | Practical | CO |
|--------:|-----------|:--:|
| 1 | Tokenization of Sentences and Words using NLTK and spaCy | CO1 |
| 2 | Stemming and Lemmatization on Sample Text | CO1 |
| 3 | Stop-word Removal from a Document | CO1 |
| 4 | Part-of-Speech (POS) Tagging of a Given Sentence | CO1 |
| 5 | Parsing and Chunking using RegEx and spaCy | CO1 |
| 6 | Named Entity Recognition (NER) using spaCy | CO1 |

## 🛠️ Technologies Used

- **Python**
- **NLTK (Natural Language Toolkit)**
- **spaCy**
- **Regular Expressions (RegEx)**

## 📁 Project Structure

```text
NLP-Unit-1/
│
├── 01_tokenization.py
├── 02_stemming_lemmatization.py
├── 03_stopword_removal.py
├── 04_pos_tagging.py
├── 05_parsing_chunking.py
├── 06_ner.py
└── README.md
```

## ⚙️ Installation

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install nltk spacy
```

Download the spaCy English language model:

```bash
python -m spacy download en_core_web_sm
```

The required NLTK datasets are downloaded by the individual programs when they are executed.

## ▶️ How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd NLP-Unit-1
```

Run any practical using:

```bash
python 01_tokenization.py
```

Similarly:

```bash
python 02_stemming_lemmatization.py
python 03_stopword_removal.py
python 04_pos_tagging.py
python 05_parsing_chunking.py
python 06_ner.py
```

## 🧠 Concepts Covered

### 1. Tokenization

Tokenization divides text into smaller units called **tokens**.

It can be used to divide:

- Text into sentences
- Sentences into words

Both **NLTK** and **spaCy** are used in this practical.

### 2. Stemming

Stemming reduces words to their root-like form by removing or modifying word endings.

Example:

```text
playing → play
studies → studi
```

### 3. Lemmatization

Lemmatization converts a word into its meaningful dictionary form.

Example:

```text
studies → study
playing → playing
```

Unlike simple stemming, lemmatization attempts to produce a valid word.

### 4. Stop-word Removal

Stop words are commonly occurring words that may be removed during text preprocessing.

Examples:

```text
the
is
a
an
of
and
```

Removing stop words can reduce unnecessary tokens during certain NLP tasks.

### 5. Part-of-Speech Tagging

POS tagging assigns a grammatical category to each word.

Examples:

```text
NN  → Noun
VB  → Verb
JJ  → Adjective
RB  → Adverb
DT  → Determiner
```

### 6. Parsing and Chunking

**Parsing** analyzes the grammatical structure and relationships between words in a sentence.

**Chunking** groups related words into phrases such as noun phrases.

Example:

```text
The young boy
```

can be identified as a noun phrase.

The practical demonstrates:

- RegEx-based chunking using NLTK
- Dependency parsing using spaCy
- Noun phrase extraction using spaCy

### 7. Named Entity Recognition

NER identifies important entities in text and assigns them categories.

Example:

```text
Google       → ORG
Greater Noida → GPE
Abhay        → PERSON
```

Common entity types include:

- PERSON
- ORG
- GPE
- DATE
- MONEY
- LOC
- PRODUCT

## 📌 Learning Outcomes

After completing these practicals, you will understand the basic NLP preprocessing pipeline and be able to:

- Tokenize text into sentences and words
- Apply stemming and lemmatization
- Remove stop words
- Perform POS tagging
- Perform parsing and chunking
- Extract named entities from text
- Use NLTK and spaCy for basic NLP tasks

## 📖 Libraries

### NLTK

NLTK provides tools and datasets for natural language processing, including tokenization, stemming, POS tagging, and corpus processing.

### spaCy

spaCy is an NLP library designed for efficient processing of text and provides features such as tokenization, POS tagging, dependency parsing, and NER.

## 👨‍💻 Author

**Abhay Chauhan**

B.Tech CSE-AI

## ⭐ Acknowledgement

These programs were created as part of the **Natural Language Processing Unit 1 practical coursework** and are intended for learning and academic purposes.
