from django.shortcuts import render
# from django.shortcuts import HttpResponse
# from django.http import JsonResponse

# from .apps import PredictorConfig
# from .models import Kitabs
from .forms import ReviewForm

# # from rest_framework.views import APIView

# import os
# from sklearn.externals import joblib
# from sklearn.metrics.pairwise import cosine_similarity

# # input and expansion query
# import pandas as pd
# import re
# from textblob import TextBlob
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# from nltk.corpus import stopwords
# from googletrans import Translator

def index(request):
    pass
#     if request.method == 'POST':
#         search_id = request.POST.get('textfield', None)
#         print(search_id)
#         # preprocessing query
#         NLTK_StopWords = stopwords.words('indonesian')
#         NLTK_StopWords = set(NLTK_StopWords)
#         hasilQuery=[]
#         s = search_id
#         s = s.lower()
#         s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
#         tokens = [token for token in s.split(" ") if token != ""]
#         T = [t for t in tokens if t not in NLTK_StopWords]
        
#         # Use the zip function to help us generate n-grams
#         # Concatentate the tokens into ngrams and return
#         for i in range (len(T)+1):
#             ngrams = zip(*[T[i:] for i in range(i)])
#             ngrams = [" ".join(ngram) for ngram in ngrams]
#             if (len(ngrams)!=0):
#                 if (ngrams not in hasilQuery):
#                     hasilQuery.append(ngrams)

#         # query translation
#         translator = Translator()
#         hasilTranslate=[]
#         for a in hasilQuery:
#             for b in a:
#                 # print (b)
#                 translations = translator.translate(b, dest='ar')
#                 # print (translations.text)
#                 hasilTranslate.append(translations.text)
#         print ("Query Translation : ", hasilTranslate[-1])
#         query = hasilTranslate[-1]
        
#         query_vec = PredictorConfig.tfidf_vectorizer.transform([query])
#         print(query_vec)

#         results = cosine_similarity(PredictorConfig.tfidf_matrix,query_vec).reshape((-1,))

#         # print("\n======================\n")
#         # print("Top 5 most similar documents in corpus:")

#         # j = 1
        
#         # for i in results.argsort()[-5:][::-1]:
#         #     print(j)
#         #     print("No ID Dokumen  : ", i)
#         #     print("Nomor Database : ", PredictorConfig.df_total.iloc[i,0])
#         #     print("Kategori       : ", PredictorConfig.df_total.iloc[i,1])
#         #     print("Nama Kitab     : ", PredictorConfig.df_total.iloc[i,2])
#         #     print("Pengarang      : ", PredictorConfig.df_total.iloc[i,3])
#         #     print("No Halaman     : ", PredictorConfig.df_total.iloc[i,4])
#         #     print("Teks Processing: ", PredictorConfig.df_total.iloc[i,5])
#         #     # print("Teks           : ", document_text[i])
#         #     print("(Score: %.4f)" % results[i])

#         #     response.update([('No ID Dokumen' + str(j), int(i)), 
#         #                     ("No Database" + str(j), int(PredictorConfig.df_total.iloc[i,0])),
#         #                     ("Kategori" + str(j), PredictorConfig.df_total.iloc[i,1]),
#         #                     ("Nama Kitab" + str(j), PredictorConfig.df_total.iloc[i,2]),
#         #                     ("Pengarang" + str(j), PredictorConfig.df_total.iloc[i,3]),
#         #                     ("No Halaman" + str(j), PredictorConfig.df_total.iloc[i,4]),
#         #                     ("Teks Processing" + str(j), PredictorConfig.df_total.iloc[i,5])])
#         #     # if(j==1):
#         #     #     response = {'NO_ID_Dokumen' : int(i),
#         #     #                 'Nomor_Database' : int(PredictorConfig.df_total.iloc[i,0]),
#         #     #                 'Nomor_Database' : PredictorConfig.df_total.iloc[i,1],
#         #     #                 'Nama_Kitab' : PredictorConfig.df_total.iloc[i,2],
#         #     #                 'Pengarang' : PredictorConfig.df_total.iloc[i,3],
#         #     #                 'No_Halaman' : PredictorConfig.df_total.iloc[i,4],
#         #     #                 'Teks_Processing' : PredictorConfig.df_total.iloc[i,5]}
#         #     j += 1

#         list_object = []
#         list_id = results.argsort()[-5:][::-1]
#         for x in list_id:
#             list_object.append(Kitabs.objects.get(id=x))
#         context = {
#             'Title':'Koleksi Kitab',
#             'Kitabs': list_object,
#         }
#         return render(request, 'search.html', context)
#     else:
#         return render(request, 'form.html')

def review(request):
    form_field = ReviewForm()

    context = {
        'review_form' : form_field,
    }

    return render(request, 'search/review.html', context)