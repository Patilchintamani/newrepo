import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from gensim import corpora, models
import pymongo

# Sample documents
documents = [
    "I love this movie! It's amazing..",
    "I had a great day today!",
    "The weather is so gloomy and depressing.",
    "I'm feeling excited about the upcoming event.",
    "I can't believe I failed the exam.",
    "The food at that restaurant was absolutely delicious!",
    "I'm feeling really stressed out with all the work deadlines.",
    "This book is incredibly boring.",
    "I'm so grateful for all the support I've received.",
    "That movie was so funny, I couldn't stop laughing.",
    "The weather is so gloomy and depressing.",
    " im feeling sad for my happiness "
    ]

# Tokenization and stopword removal
stop_words = set(stopwords.words('english'))
tokenized_documents = [word_tokenize(doc.lower()) for doc in documents]
filtered_documents = [[word for word in doc if word not in stop_words] for doc in tokenized_documents]

# Sentiment Analysis
sentiments = [TextBlob(' '.join(doc)).sentiment.polarity for doc in filtered_documents]

# Topic Modeling
dictionary = corpora.Dictionary(filtered_documents)
corpus = [dictionary.doc2bow(doc) for doc in filtered_documents]
lda_model = models.LdaModel(corpus, num_topics=2, id2word=dictionary)

# Print results
print("Sentiments:")
for i, sentiment in enumerate(sentiments):
    print(f"Document {i+1}: {'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'}")

print("\nTopics:")
for i, topic in enumerate(lda_model.print_topics()):
    print(f"Topic {i+1}: {topic[1]}")

# Establish connection to MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017")

# Select or create database
db = client["ram"]

# Select or create collection
collection = db["shubham"]

# Insert text data into the collection
for doc in documents:
    collection.insert_one({"text": doc})

print("Text data stored in the database.")
