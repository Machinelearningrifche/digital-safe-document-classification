from sklearn.feature_extraction.text import TfidfVectorizer

from tqdm import tqdm
from nltk import SnowballStemmer
import pandas as pd
import re

stemmer = SnowballStemmer('english')


def preprocess(text: str) -> str:
    return re.sub(r'\b\d+\b', 'DIGITS', stemmer.stem(text.lower()))


def train_tf_idf(training_documents):
    vectorizer = TfidfVectorizer(max_df=0.6, min_df=2, max_features=3000, preprocessor=preprocess)
    vectorizer.fit_transform(tqdm(training_documents, desc='Fitting tf-idf'))
    return vectorizer


class Model:
    def __init__(self):
        self.vectorizer = None

    def train_vectorizer(self, training_documents):
        print(f'Training vectorizer with {len(training_documents)} articles')
        self.vectorizer = train_tf_idf(training_documents)
        return self.vectorizer

    def vectorize(self, documents):
        if isinstance(documents, str):
            documents = [documents]
        return self.vectorizer.transform(documents)
