import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

with open('input_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

#Токенізація по словам
words = word_tokenize(text)

#Лематизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
stemmed_words = [stemmer.stem(word) for word in words]

#Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in lemmatized_words if word.lower() not in stop_words]

#Видалення пунктуації
filtered_words = [word for word in filtered_words if word not in string.punctuation]

processed_text = ' '.join(filtered_words)
with open('processed_text.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)
