from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

from .apps import PredictorConfig

from .models import Kitabs

import os
from sklearn.externals import joblib
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

def index(request):
    # pass
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        print(search_id)

        # exquery = request.POST.get('exquery')
        # print(exquery)

        # preprocessing query
        NLTK_StopWords = stopwords.words('indonesian')
        NLTK_StopWords = set(NLTK_StopWords)
        hasilQuery=[]
        s = search_id
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
        tokens = [token for token in s.split(" ") if token != ""]
        T = [t for t in tokens if t not in NLTK_StopWords]
        
        # Use the zip function to help us generate n-grams
        # Concatentate the tokens into ngrams and return
        for i in range (len(T)+1):
            ngrams = zip(*[T[i:] for i in range(i)])
            ngrams = [" ".join(ngram) for ngram in ngrams]
            if(len(ngrams)!=0):
                if(ngrams not in hasilQuery):
                    hasilQuery.append(ngrams)

        # query translation
        translator = Translator()
        hasilTranslate=[]
        for a in hasilQuery:
            for b in a:
                # print (b)
                translations = translator.translate(b, dest='ar')
                # print (translations.text)
                hasilTranslate.append(translations.text)
        print ("Query Translation : ", hasilTranslate[-1])
        query = hasilTranslate[-1]

        exquery = request.POST.get('exquery', None)
        print(exquery)

        # Query Expansion
        if(exquery=='Iya'):
            print("Pakai Ekspansi Query")
            # pq = PredictorConfig.modelFT.wv.most_similar(query)
            # print(pq)
            # words = []
            # for i in range(4):
            #     words.append(pq[i][0])
            # words.append(query)
            # print(words)
            # query = []
            # query.append(' '.join(words))

            # query_vec = PredictorConfig.tfidf_vectorizer.transform(query)

        # else:
        query_vec = PredictorConfig.tfidf_vectorizer.transform([query])
        
        print(query_vec)

        results = cosine_similarity(PredictorConfig.tfidf_matrix,query_vec).reshape((-1,))

        # print("\n======================\n")
        # print("Top 5 most similar documents in corpus:")

        # j = 1
        
        # for i in results.argsort()[-5:][::-1]:
        #     print(j)
        #     print("No ID Dokumen  : ", i)
        #     print("Nomor Database : ", PredictorConfig.df_total.iloc[i,0])
        #     print("Kategori       : ", PredictorConfig.df_total.iloc[i,1])
        #     print("Nama Kitab     : ", PredictorConfig.df_total.iloc[i,2])
        #     print("Pengarang      : ", PredictorConfig.df_total.iloc[i,3])
        #     print("No Halaman     : ", PredictorConfig.df_total.iloc[i,4])
        #     print("Teks Processing: ", PredictorConfig.df_total.iloc[i,5])
        #     # print("Teks           : ", document_text[i])
        #     print("(Score: %.4f)" % results[i])

        #     j += 1

        list_object = []
        list_id = results.argsort()[-5:][::-1]
        for x in list_id:
            x += 1
        for x in list_id:
            list_object.append(Kitabs.objects.get(id=x))
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
        relevan = False
        if(request.POST['relevan']=='Iya'):
            relevan = True

        Review.objects.create(
            username = request.user,
            query = request.POST['query'],
            review = request.POST['review'],
            dokumen_relevan = relevan
        )
        return HttpResponseRedirect("/")

    return render(request, 'search/review.html', context)