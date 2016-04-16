#!/usr/bin/python
import sys
def sentrank(argv):
    ##path=argv[1]
    sentence={}
    f1=open("C:/Users/chetan/Desktop/tamil-text-summarization-master/article-1.txt","r",encoding="utf8")
    s=f1.read()
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
                word_dic.setdefault(word,0)
            sentence.setdefault(sen_no,{'position':0,'para_position':0,'length':0,'para_pos_score':0,'pos_score':0,'len_score':0,'surface_score':0})
            sentence[sen_no]['position']=sen_no
            sentence[sen_no]['para_position']=para_pos
            sentence[sen_no]['length']=len(word_lst)
            sen_no+=1
            para_pos+=1
        for iter in range(1,para_pos):
            sentence[iter]['para_pos_score']=1-sentence[iter]['para_position']/para_pos     
    for iter in range(1,sen_no):
        sentence[iter]['pos_score']=1-sentence[iter]['position']/sen_no
        sentence[iter]['len_score']=sentence[iter]['length']/len(word_dic)
        sentence[iter]['surface_score']=sentence[iter]['pos_score']+sentence[iter]['para_pos_score']+sentence[iter]['len_score']


if __name__=="__main__":
    sentrank(sys.argv)

#to do : stemming
