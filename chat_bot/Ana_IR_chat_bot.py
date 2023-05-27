# _____TF-IDF libraries_____
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# _____helper Libraries_____
import pickle  # would be used for saving temp files
import csv     # used for accessing the dataset
import timeit  # to measure time of training
import random  # used to get a random number

#train Model
sentences = [] #store user input text to bot
answers = [] #to store corresponding responses by bot

with open("DataSet/randychat.csv" , 'r') as sentence_file:
    reader = csv.reader(sentence_file, delimiter = ',')
    
    for row in reader:
        sentences.append(row[0])
        answers.append(row[1])
        
    tfidf_vect = TfidfVectorizer()
    tfidf_matrix_train= tfidf_vect.fit_transform(sentences)
    
    
def talk_to_Ana(test_set_sentence):
    try:

        # enter your test sentence
        test_set = (test_set_sentence, "")
        tfidf_matrix_test = tfidf_vect.transform(test_set)
        cosine = cosine_similarity(tfidf_matrix_test,tfidf_matrix_train)

        mx = cosine.max()

        # we can afford to get multiple high score documents to choose from
        new_max = mx - 0.01

        # load them to a list
        choices = np.where(cosine > new_max)
        t = []
        for i in choices:
            t.append(int(i))  
        # choose a random one to return to the user 
        # this happens to make Lina answers differently to same sentence
        response_index = random.choice(t)
        return answers[response_index]
    
    
    except TypeError:
        print('Sorry, I dont understand you')
        

reply = talk_to_Ana('is it essential to you ?  to help humans ?')
print(reply)


flag = True
print('Hi I am Ana, How can I help you')
while flag:
    termination_words = ['stop','quit','bye','done','shut-up','get-lost']

    sentence = input('->  ')
    check_sent = sentence.lower().split()
    for word in check_sent:
        if word in termination_words:
            print('Ok, If you need any help, plese feel free to ask, Good Bye!')
            flag = False
            break
            
    reply = talk_to_Ana(sentence)
    print(reply)
