def kannada_method2():
    f1=open("C:/Users/chetan/Desktop/tamil-text-summarization-master/article-1.txt","r",encoding="utf8")
    word_dic={}
    sentence_score={}
    no=0
    for line in f1:
        word_lst=line.split(" ")
        no+=len(word_lst)
        for word in word_lst:
            word=word.strip(".")
            word_dic.setdefault(word,0)
            word_dic[word]+=1

    s=f1.read()
    n=1
    sent_lst=s.split(".")
    for word in word_dic:
        word_dic[word]/=no
    for sent in sent_lst:
        sentence_score.setdefault(n,{'score':0,'length':0,'odia_score':0})
        sent=sent.strip()
        word_lst=sent.split(" ")
        sentence_score[n]['length']=len(word_lst)
        for word in word_lst:
            sentence_score[n]['score']+=word_dic[word]
            sentence_score[n]['odia_score']+=word_dic[word]/sentence_score[n]['length']
        n+=1
#haven't checked for correctness
