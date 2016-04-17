import sys
def kannada_method2(argv):
    path=argv[1]
    no_of_sentences=argv[2]
    f1=open(path,"r",encoding="utf8")
    f1=open("C:/Users/chetan/Desktop/tamil-text-summarization-master/article-1.txt","r",encoding="utf8")
    word_dic={}
    sentence_score={}
    no=0
    s=f1.read()
    f1.close()
    line_lst=s.split(".")
    for line in line_lst:
        word_lst=line.split(" ")
        no+=len(word_lst)
        for word in word_lst:
            word=word.strip(".")
            word_dic.setdefault(word,0)
            word_dic[word]+=1

    
    n=1
    
    sent_lst=s.split(".")
    for word in word_dic:
        word_dic[word]/=no
    for sent in sent_lst:
        ##print(sent_lst)
        sentence_score.setdefault(n,{'score':0,'length':0,'odia_score':0,'content':''})
        sent=sent.strip()
        sentence_score[n]['content']=sent
        word_lst=sent.split(" ")
        sentence_score[n]['length']=len(word_lst)
        ##print(word_lst)
        for word in word_lst:
            print(n)
            sentence_score[n]['score']+=word_dic[word]
            sentence_score[n]['odia_score']+=word_dic[word]/sentence_score[n]['length']
        n+=1



        
if __name__=="__main__":
    kannada_method2(sys.argv)
