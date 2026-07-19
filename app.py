import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def trasform(text):
  text = text.lower()

  text = nltk.word_tokenize(text)

  x=[]
  for i in text:
    if i.isalnum():
      x.append(i)
  
  text = x[:]
  x.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      x.append(i)

  text = x[:]
  x.clear()

  for i in text:
    x.append(PorterStemmer().stem(i))

  return " ".join(x)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")
if st.button("Predict"):

    # preprocess
    transformed_sms = trasform(input_sms)


    # vectorize
    vector_input = tfidf.transform([transformed_sms])

    # predict
    result = model.predict(vector_input)[0]

    # display
    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")
    