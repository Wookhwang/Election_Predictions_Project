from konlpy.tag import Okt
import json
import nltk
import numpy as np
import tensorflow as tf
from time import sleep

class Analyzer:
    def __init__(self, file_name, model_name):
        with open(file_name, encoding='UTF8') as json_file:
            train_docs = json.load(json_file)
        tokens = [t for d in train_docs for t in d[0]]
        text = nltk.Text(tokens, name='NMSC')
        self.selected_words = [f[0] for f in text.vocab().most_common(10000)]
        self.model = tf.keras.models.load_model(model_name)

    def tokenize(self, doc):
        okt = Okt()
        #sleep(0.3)
        return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

    def term_frequency(self, doc):
        print(doc)
        return [doc.count(word) for word in self.selected_words]

    def predict_pos_neg(self, review):
        token = self.tokenize(review)
        tf = self.term_frequency(token)
        data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
        score = float(self.model.predict(data))
        if (score > 0.5):
            return "1"
        else:
            return "0"

