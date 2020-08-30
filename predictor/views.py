from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

from .apps import PredictorConfig

from .models import Kitabs

import os
import joblib
from tashaphyne.stemming import ArabicLightStemmer
from sklearn.metrics.pairwise import cosine_similarity

# input and expansion query
import pandas as pd
import re
from textblob import TextBlob
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from googletrans import Translator
from nltk.tokenize import wordpunct_tokenize

def index(request):
    # pass
    def preprocessing_query(input_query):
        NLTK_StopWords = stopwords.words('indonesian')
        NLTK_StopWords = set(NLTK_StopWords)
        hasilQuery=[]
        s = input_query
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
        tokens = [token for token in s.split(" ") if token != ""]
        T = [t for t in tokens if t not in NLTK_StopWords]
        
        # Use the zip function to help us generate n-grams
        # Concatentate the tokens into ngrams and return
        for i in range (len(T)+1):
            ngrams = zip(*[T[i:] for i in range(i)])
            ngrams = [" ".join(ngram) for ngram in ngrams]
            if (len(ngrams)!=0):
                if (ngrams not in hasilQuery):
                    hasilQuery.append(ngrams)
        return hasilQuery

    # Query Translation
    def query_translation(hasilQuery):
        translator = Translator()
        hasilTranslate=[]
        for a in hasilQuery:
            for b in a:
                # print (b)
                translations = translator.translate(b, dest='ar')
                # print (translations.text)
                hasilTranslate.append(translations.text)
        print ("Query Translation : ", hasilTranslate[-1])
        return hasilTranslate[-1]

    # Local Search Engine
    def search_engine(search_id):  
        print("Input query: ", search_id)
        hasilQuery = preprocessing_query(search_id)
        print("Preprocessing query: ", hasilQuery[-1])
        query = query_translation(hasilQuery)
        print("Query translation: ", query)
        
        ArListem = ArabicLightStemmer()
        stem = ArListem.light_stem(query) 
        hasil = ArListem.get_root()
        print("Stem: ", hasil)

        exquery = request.POST.get('exquery', None)
        print(exquery)
        
        # Query Expansion
        if(exquery=='Iya'):
            print("Pakai Ekspansi Query")
            # pass
            token = wordpunct_tokenize(hasil)
            query = []
            for word in token:
                 pq = PredictorConfig.modelFT.wv.most_similar(word)
                 print(pq)
                 words = []
                 for i in range(4):
                     words.append(pq[i][0])
                 words.append(word)
                 print(words)
                
                 query.append(' '.join(words))
                 queries = []
                 queries.append(' '.join(query))
                 print("Query Expansion: ", queries)
                 hasil = queries[0]

        query_vec = PredictorConfig.tfidf_vectorizer.transform([hasil])
        
        print(query_vec)

        results = cosine_similarity(PredictorConfig.tfidf_matrix,query_vec).reshape((-1,))

        list_object = []
        list_id = results.argsort()[-10:][::-1]
        list_id = [x+1 for x in list_id]
        for x in list_id:
            list_object.append(Kitabs.objects.get(id=x))
        
        return list_object

    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        print(search_id)
        list_object = search_engine(search_id)
        context = {
            'title': search_id + " | Hasil Pencarian Kitab Ulama",
            'Kitabs': list_object,
        }
        return render(request, 'search/index.html', context)
    else:
        context = {
            'title': 'Kitab Ulama',
        }
        return render(request, 'index.html')

def review(request):
    form_field = ReviewForm()

    context = {
        'title' :'Review Hasil Pencarian Dokumen | Kitab Ulama',
        'review_form' : form_field,
    }

    if(request.method=="POST"):
        print(request.POST)

        Review.objects.create(
            username = request.user,
            query = request.POST.get("Query"),
            review = request.POST.get("review"),
            dokumen_relevan = request.POST.get('relevan')
        )
        return HttpResponseRedirect("/")

    return render(request, 'search/review.html', context)
