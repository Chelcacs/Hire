from datasets import load_dataset


data = load_dataset("tner/bionlp2004")
data
def id2label(idx):
    return {
    0:"O", 
    1:"B-DNA", 
    2:"I-DNA", 
    3:"B-protein", 
    4:"I-protein", 
    5:"B-cell_type", 
    6:"I-cell_type", 
    7:"B-cell_line", 
    8:"I-cell_line", 
    9:"B-RNA", 
    10:"I-RNA"
    }.get(idx, '')
    
    
def getSentences(dataset):
    sentences = []
    tokens = dataset['tokens']
    ner_tags = dataset['tags']
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
    
def reverse_data_format(save_path):
    f = open(save_path, 'r')
    lines = f.readlines()
    sentence = []
    sentenceS = []
    for line in lines:
        if not line == "\n":
            couple = tuple(line.strip('\n').split('\t'))
            sentence.append(couple)
        else:
            sentenceS.append(sentence) 
            sentence = []
    return sentenceS
            
            
        
            
train_sents = getSentences(data['train'].train_test_split(test_size=0.5,shuffle=True)['train'])
val_sents = getSentences(data['validation'].train_test_split(test_size=0.5,shuffle=True)['train'])
test_sents = getSentences(data['test'].train_test_split(test_size=0.5,shuffle=True)['train'])

data_format('train.txt', train_sents)
data_format('val.txt', val_sents)
data_format('test.txt', test_sents)

res = reverse_data_format('test.txt')
# data_format('data/subset.txt', train_sents[:1000])