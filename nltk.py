
from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')
nltk.download('punkt', quiet=True)

#Get the Article
article = Article("https://www.alaraby.co.uk/%D8%A7%D9%84%D8%AE%D8%B1%D9%88%D8%AC-%D9%85%D9%86-%D9%85%D9%90%D8%B9%D8%B7%D9%8E%D9%81-%D8%A7%D9%84%D8%AE%D9%88%D9%81")
article.download()
article.parse()
article.nlp()
corpus = article.text
#print the article text
print(corpus)
#tokanization
text = corpus
sentence_list = nltk.sent_tokenize(text)
print(sentence_list)

# function to return a random greeting response to user greeting
def greeting_response(text):
    text = text.lower()
bot_greetings = ["مرحبا", "أحد"]
print(bot_greetings)
