# Usage
### Requirements
    Python>=3.6
    Pytorch>=0.4.1
    sklearn
    seqeval
    nltk
    datasets
    numpy
### Process Datasets
all datasets are put in folder `data`,and 
run `python generate_data.py` in corresponding folder to generate data in correct format

### Train
`python main.py --config train_configs/{DATASET}.train.config`

### Evaluation
`python main.py --config test_configs/{DATASET}.test.config`

# Results
### bionlp2004:
                   precision    recall   f1-score   support

             DNA     0.6550    0.6802    0.6673       494
             RNA     0.6984    0.7719    0.7333        57
       cell_line     0.5203    0.6235    0.5672       247
       cell_type     0.7943    0.6443    0.7115       953
         protein     0.6723    0.7616    0.7142      2492

       micro avg     0.6817    0.7179    0.6993      4243
       macro avg     0.6681    0.6963    0.6787      4243
    weighted avg     0.6892    0.7179    0.6998      4243

### nerdataset:
                    precision    recall  f1-score   support

             art     0.0000    0.0000    0.0000        10
             eve     0.3333    0.2000    0.2500        10
             geo     0.8738    0.8831    0.8784      1215
             gpe     0.9703    0.9271    0.9482       494
             nat     0.0000    0.0000    0.0000         4
             org     0.6766    0.6800    0.6783       600
             per     0.8000    0.6863    0.7388       542
             tim     0.8876    0.8644    0.8758       612

       micro avg     0.8433    0.8150    0.8289      3487
       macro avg     0.5677    0.5301    0.5462      3487
    weighted avg     0.8394    0.8150    0.8264      3487

### mmner:
                    precision    recall  f1-score   support

             LOC     0.7331    0.7436    0.7383       702
             ORG     0.7262    0.5737    0.6410       624
             PER     0.7936    0.8245    0.8087       718

       micro avg     0.7545    0.7202    0.7369      2044
       macro avg     0.7510    0.7139    0.7294      2044
    weighted avg     0.7522    0.7202    0.7334      2044

### nercorpus:
                    precision    recall  f1-score   support

             art     0.1000    0.0588    0.0741        17
             eve     0.4000    0.1538    0.2222        13
             geo     0.8194    0.8906    0.8535      1243
             gpe     0.9498    0.9220    0.9357       513
             nat     0.0000    0.0000    0.0000         6
             org     0.6735    0.6448    0.6588       563
             per     0.7427    0.7033    0.7225       546
             tim     0.8894    0.8333    0.8605       666

       micro avg     0.8141    0.8088    0.8114      3567
       macro avg     0.5719    0.5258    0.5409      3567
    weighted avg     0.8101    0.8088    0.8084      3567

### wikineural:
                    precision    recall  f1-score   support

             LOC     0.8481    0.8963    0.8715      1196
            MISC     0.7593    0.6418    0.6957       349
             ORG     0.7360    0.6691    0.7010       275
             PER     0.9150    0.9384    0.9265       941

       micro avg     0.8518    0.8558    0.8538      2761
       macro avg     0.8146    0.7864    0.7987      2761
    weighted avg     0.8485    0.8558    0.8511      2761

### conll2003:
                    precision    recall  f1-score   support

             LOC     0.8991    0.8544    0.8762       824
            MISC     0.7573    0.6923    0.7233       338
             ORG     0.7533    0.7672    0.7602       812
             PER     0.7918    0.8855    0.8360       786

       micro avg     0.8066    0.8178    0.8122      2760
       macro avg     0.8004    0.7999    0.7989      2760
    weighted avg     0.8083    0.8178    0.8119      2760





