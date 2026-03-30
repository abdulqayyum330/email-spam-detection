import nltk
import streamlit as st
import string
import pickle
import sklearn
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

ps = PorterStemmer()

def clean_and_process_text(text_input):
    text_input = text_input.lower()
    text_input = nltk.word_tokenize(text_input)
    
    y = []
    for i in text_input:
        if i.isalnum():
            y.append(i)
            
    text_input = y[:]
    y.clear()
    for i in text_input:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text_input = y[:]
    y.clear()
    for i in text_input:
        y.append(ps.stem(i))
        
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('spam_model.pkl', 'rb'))

st.title('AI Message & Email Spam Detector')
user_input = st.text_area('Enter the message to classify')

if st.button('Predict'):
    processed_msg = clean_and_process_text(user_input)
    vector_input = tfidf.transform([processed_msg])
    prediction = model.predict(vector_input)[0]
    
    if prediction == 1:
        st.header('Result: Spam')
    else:
        st.header('Result: Not Spam')
