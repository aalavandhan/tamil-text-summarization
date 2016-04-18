#!/usr/bin/python
import sys
import operator
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


def sentrank(argv):
    path=argv[1]
    no_of_sentences=int(argv[2])

    sentence={}

    f1=open(path,"r")
    s=f1.read()

    # import pdb
    # pdb.set_trace()

    para_lst=s.split("\n")
    sen_no=1
    word_dic={}

    for para in para_lst:
        para=para.strip()
        para_pos=1
        sen_lst=para.split(".")
        for sen in sen_lst:
            word_lst=sen.split(" ")
            for word in word_lst:
                word=word.strip("\"")
                word_dic.setdefault(word,0)
            sentence.setdefault(sen_no,{'position':0,'para_position':0,'length':0,'para_pos_score':0,'pos_score':0,'len_score':0,'surface_score':0,'content':''})
            sentence[sen_no]['position']=sen_no
            sentence[sen_no]['para_position']=para_pos
            sentence[sen_no]['length']=len(word_lst)
            sentence[sen_no]['content']=sen
            sen_no+=1
            para_pos+=1
        for i in range(1,para_pos):
            sentence[i]['para_pos_score']= 1 - ( sentence[i]['para_position'] / para_pos )

    for i in range(1,sen_no):
        sentence[i]['pos_score'] = 1 - ( sentence[i]['position'] / sen_no )
        sentence[i]['len_score'] = ( sentence[i]['length'] / len(word_dic) )

        sentence[i]['surface_score'] = sentence[i]['pos_score'] + sentence[i]['para_pos_score'] + sentence[i]['len_score']

    sorted_lst=sorted(sentence.items(), key=lambda x: x[1]['surface_score'],reverse=True)

    for i in range(0, no_of_sentences):
        print(sentence[sorted_lst[i][0]]['content'])
        print(sentence[sorted_lst[i][0]]['surface_score'])

if __name__=="__main__":
  sentrank(sys.argv)



'''to do 1) stemming
    2)Removal (stripping) of ""
    '''
