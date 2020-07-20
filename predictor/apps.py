from django.apps import AppConfig
from django.conf import settings

import os
from sklearn.externals import joblib

class PredictorConfig(AppConfig):  
    name = 'predictor'  
    # path_df = os.path.join(settings.MODELS, 'df_total8.csv')
    path_tfidf = os.path.join(settings.MODELS, 'tfidf8.pkl')
    path_vectorizer = os.path.join(settings.MODELS, 'vectorizer8.pkl')

#     # df_total = pd.read_csv(path_df)
    tfidf_matrix = joblib.load(path_tfidf)
    tfidf_vectorizer = joblib.load(path_vectorizer)