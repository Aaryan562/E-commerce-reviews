from django.shortcuts import render
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import pandas as pd
from nltk.corpus import stopwords
ps=PorterStemmer()
wnl=WordNetLemmatizer()
import pickle
rf = pickle.load(open(r'C:\Users\JARVIS\e_commerce_reviews\e_commerce_reviews\Pickle_RF_Model.pkl', 'rb'))
tfidf=pickle.load(open(r'C:\Users\JARVIS\e_commerce_reviews\e_commerce_reviews\Pickle_tfidf_transform_Model.pkl','rb'))
import re
def clean(data):
    corpus=[]
    review=re.sub('[^a-zA-Z]',' ',data)
    review=review.lower()
    review=review.split()
    review=[wnl.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
    return corpus
def main(request):
    if request.method=='POST':
        text=request.POST['review']
        text=clean(text)
        text_vec=tfidf.transform(text).toarray()
        pred=rf.predict(text_vec)
        print(pred)
        return render(request,'main.html',{'result':pred})
    return render(request,'main.html')

# def result(request):

# Create your views here.
