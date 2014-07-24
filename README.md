Semi-supervised LDA, which allows labelling of some documents in training, and a rule file to assign seed words for each topic.

Besides topics appear in training data and the rule file, new topics also can learned.

##Data format

* training data:

label1,label2 word1:num1 word2:num2 ...

 word3:num3 word4:num4 ...

* rule file:

label1 word1,word2 ...

label2 word3,word4 ...

##Example

* train:

python lda\_train.py -train train.txt -rule rule.txt -k 20 -alpha 0.5 -beta 0.1 -burnin 50 -iter 100 -model model.txt

* inference:

python lda\_infer.py -model model.txt -alpha 0.5 -beta 0.1 -burnin 50 -test test.txt -output result.txt

##Evaluation

`log-likelihood`
