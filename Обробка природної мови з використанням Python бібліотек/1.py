import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt

nltk.download('gutenberg')
alice_text = gutenberg.raw('carroll-alice.txt')

#Функція для підрахунку кількості слів у тексті
def count_words(text):
    words = nltk.word_tokenize(text)
    return len(words)

#Функція для визначення 10 найбільш вживаних слів та побудови діаграми
def plot_top_words(words, frequencies, title):
    plt.bar(words, frequencies)
    plt.xlabel('Слова')
    plt.ylabel('Частота')
    plt.title(title)
    plt.show()

#Функція для обробки тексту: видалення стоп-слів та пунктуації
def preprocess_text(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return words

while True:
    user_input = input("'1' для визначення 10 найбільш вживаних слів\n '2' для визначення та побудови діаграми після видалення стоп-слів та пунктуації\n '3' для виходу\n Введіть значення: ")

    if user_input == '1':
        #Визначення 10 найбільш вживаних слів
        words = nltk.word_tokenize(alice_text)
        fdist = FreqDist(words)
        top_words = fdist.most_common(10)
        print("10 найбільш вживаних слів у тексті:")
        for word, frequency in top_words:
            print(f"{word}: {frequency}")
        
        #Побудова діаграми
        words, frequencies = zip(*top_words)
        plot_top_words(words, frequencies, '10 найбільш вживаних слів у тексті')

    elif user_input == '2':
        processed_words = preprocess_text(alice_text)

        #Визначення 10 найбільш вживаних слів після обробки
        fdist_processed = FreqDist(processed_words)
        top_words_processed = fdist_processed.most_common(10)
        print("10 найбільш вживаних слів у тексті після видалення стоп-слів та пунктуації:")
        for word, frequency in top_words_processed:
            print(f"{word}: {frequency}")

        #Побудова діаграми після обробки
        words_processed, frequencies_processed = zip(*top_words_processed)
        plot_top_words(words_processed, frequencies_processed, '10 найбільш вживаних слів у тексті після видалення стоп-слів та пунктуації')

    elif user_input.lower() == '3':
        break

    else:
        print("Невірний ввід. Спробуйте ще раз.")
