import pandas as pd
from ast import literal_eval

data = pd.read_csv('ner.csv')
data = data.drop(['POS', 'Sentence #'], axis=1)
data = data.sample(frac=1).reset_index(drop=True)
data = data[:10000]
data['Tag'] = data['Tag'].apply(literal_eval)
data['Sentence'] = data['Sentence'].apply(lambda x: x.split(' '))

data_list = data.values.tolist()

def getSentences(data_list):
    sentences = []
    for value in data_list:
        token_list = []
        tokens = value[0]
        tags = value[1]
        for i in range(0, len(tokens)):
            token_list.append((tokens[i], tags[i]))
        sentences.append(token_list)
    return sentences

def data_format(save_path, dataset):
    with open(save_path, 'w') as f:
        for sentence in dataset:
            for couple in sentence:
                f.write('\t'.join(list(couple))+'\n')
            f.write('\n')
    f.close()

train_sents = getSentences(data_list[:7000])
test_sents = getSentences(data_list[7000:8500])
val_sents = getSentences(data_list[8500:])
data_format('train.txt', train_sents)
data_format('val.txt', val_sents)
data_format('test.txt', test_sents)
