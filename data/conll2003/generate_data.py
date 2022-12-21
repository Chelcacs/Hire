
# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
from itertools import chain

import nltk
import sklearn
import scipy.stats
# from sklearn.metrics import make_scorer, classification_report, accuracy_score
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score
from datasets import load_dataset
from seqeval.metrics import classification_report
import json

# import data

data = load_dataset("conll2003")
data
def id2label(idx):
    return {
        0:'O',
        1:'B-PER',
        2:'I-PER',
        3:'B-ORG',
        4:'I-ORG',
        5:'B-LOC',
        6:'I-LOC',
        7:'B-MISC', 
        8:'I-MISC',
    }.get(idx, '')
    
    
def getSentences(dataset):
    sentences = []
    tokens = dataset['tokens']
    ner_tags = dataset['ner_tags']
    for i in range(0, len(tokens)):
        for j in range(0, len(tokens[i])):
            tokens[i][j] = (tokens[i][j], id2label(ner_tags[i][j]))
        sentences.append(tokens[i])
    return sentences

def data_format(save_path, dataset):
    with open(save_path, 'w') as f:
        for sentence in dataset:
            for couple in sentence:
                f.write('\t'.join(list(couple))+'\n')
            f.write('\n')
    f.close()
            
train_sents = getSentences(data['train'].train_test_split(test_size=0.5,shuffle=True)['train'])
val_sents = getSentences(data['validation'].train_test_split(test_size=0.5,shuffle=True)['train'])
test_sents = getSentences(data['test'].train_test_split(test_size=0.5,shuffle=True)['train'])

data_format('train.txt', train_sents)
data_format('val.txt', val_sents)
data_format('test.txt', test_sents)
# data_format('data/subset.txt', train_sents[:1000])