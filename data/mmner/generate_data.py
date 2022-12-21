import tarfile
import pandas as pd

def group_data(df):
    df['Word'] = df['Word'].apply(lambda x: str(x))
    df['Tag'] = df['Tag'].apply(lambda x: str(x))
    result = {'Sentence': [], 'Tag': []}
    sentence = []
    tag = []
    for index, row in df.iterrows():
        if row['Word'] == 'nan':
            result['Sentence'].append(sentence)
            result['Tag'].append(tag)
            sentence = []
            tag = []
        else:
            sentence.append(row['Word'].replace('de:', ''))
            tag.append(row['Tag'])
    return pd.DataFrame(result)

tar = tarfile.open('de.tar')

train = tar.extractfile(tar.getmember('train'))
train = pd.read_csv(train, sep='\t', skip_blank_lines=False, header=None, names=['Word', 'Tag'])
train = group_data(train)
train = train.sample(frac=1).reset_index(drop=True)
train = train[:7000]

val = tar.extractfile(tar.getmember('dev'))
val = pd.read_csv(val, sep='\t', skip_blank_lines=False, header=None, names=['Word', 'Tag'])
val = group_data(val)
val = val.sample(frac=1).reset_index(drop=True)
val = val[:1500]

test = tar.extractfile(tar.getmember('test'))
test = pd.read_csv(test, sep='\t', skip_blank_lines=False, header=None, names=['Word', 'Tag'])
test = group_data(test)
test = test.sample(frac=1).reset_index(drop=True)
test = test[:1500]

# train.head(10)



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
    
train_sents = getSentences(train.values.tolist())
test_sents = getSentences(test.values.tolist())
val_sents = getSentences(val.values.tolist())
data_format('train.txt', train_sents)
data_format('val.txt', val_sents)
data_format('test.txt', test_sents)