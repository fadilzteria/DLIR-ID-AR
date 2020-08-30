from django.apps import AppConfig
from django.conf import settings

import os
import joblib
from gensim.models import FastText

class PredictorConfig(AppConfig):  
    name = 'predictor'  
    path_modelFT = os.path.join(settings.MODELS, 'modelFT_syafii.pkl')
    path_tfidf = os.path.join(settings.MODELS, 'tfidf_syafii.pkl')
    path_vectorizer = os.path.join(settings.MODELS, 'vectorizer_syafii.pkl')

    modelFT = joblib.load(path_modelFT)
    tfidf_matrix = joblib.load(path_tfidf)
    tfidf_vectorizer = joblib.load(path_vectorizer)