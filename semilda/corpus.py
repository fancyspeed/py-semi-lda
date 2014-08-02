#coding: utf-8

class Document:
    
    def __init__(self, word_list=[], label_list=[]):
        self.word_list = word_list 
        self.label_list = label_list 


class Corpus:

    def __init__(self):
        self.doc_list = []

    def init_corpus_and_model(self, p_train, model): 
        for line in open(p_train):
            row = line.rstrip().split(' ')

            labels = row[0]
            label_list = []
            for label in labels.split(','): 
                if not label: continue
                label_int = model.add_topic(label)
                label_list.append(label_int)

            words = row[1:]
            word_list = []
            for element in words:
                if element.count(':') == 1:
                    word, count = element.split(':')
                else: 
                    word, count = element, 1
                word_int = model.add_word(word)
                word_list.extend( [word_int] * int(count) )

            doc = Document(label_list, word_list)
            self.doc_list.append(doc)
            print label_list, word_list
        print 'topics', model.topic_num
        print 'docs', len(self.doc_list)
        print 'words', len(model.word_seed_list)
            





