import nltk
import json
import pickle
import numpy as np

nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers import Activation, Dense, Dropout
import random

#Upload intents file and create our lists
words=[]
classes = []
doc = []
ignore_words = ['?', '!', ',', '.']
data_words = open(r'C:\...\intents.json').read()
intents = json.loads(data_words)

for intent in intents['intents']:
    for pattern in intent['patterns']:

        #Tokenize all the words (separate them)
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        #Add all the words into doc 
        doc.append((w, intent['tag']))

        #Add the classes
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(doc)      

#lemmatization      

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))


classes = sorted(list(set(classes)))

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))       

#Training
training = []
output_empty = [0] * len(classes)
for doc in doc:
    #Initialize bag of words
    bag = []
    #Create list of words
    pattern_words = doc[0]
    #Word lemmatization
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)   
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
#Create np array
random.shuffle(training)
training = np.array(training)
#Create training and testing lists
train_x = list(training[:,0])
train_y = list(training[:,1])

#Create the model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dense(35, activation='relu'))
model.add(Dense(len(train_y[0]), activation='softmax'))

#Compile the model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#Save the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=150, batch_size=10, verbose=1)
model.save('Mychatbot_model.h5', hist)

from keras.models import load_model
model = load_model('Mychatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

#Define chatbot functions
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

import tkinter
from tkinter import *

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "Me: " + msg + '\n\n')
        ChatLog.config(foreground="#3E4149", font=("Arial", 12 ))

        res = chatbot_response(msg)
        ChatLog.insert(END, "ChatBot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("Chat with Customer Service")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create ChatBot window
ChatLog = Text(base, bd=6, bg="white", height="8", width="70", font="Calibri")

ChatLog.config(state=DISABLED)

#Scrollbar
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="arrow")

#Create Send button
SendButton = Button(base, font=("Calibri",12,'bold'), text="Send", width="15", height=5,
                    bd=0, bg="pink", activebackground="light green",fg='black',
                    command= send )

EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")

scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
