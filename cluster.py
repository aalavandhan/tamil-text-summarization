import nltk
import sys
import os
import math
import pdb
from nltk.util import ngrams
from pprint import pprint
from sklearn.cluster import KMeans
from sys import argv
import pdb

input_list=[]
ngram_dict=dict()
sentence=dict()
line_count=0
weight_list=[]
vector_list=[[]]
word_list=[]
cluster_no=3
cluster_dict={}


def sentence_weight():
    temp=1
    term = ""
    global input_list, ngram_dict,line_count,sentence,word_list,vector_list,cluster_no
    word_list = list(ngram_dict.keys())
    vector_list = [[0 for x in range(len(word_list))] for x in range(len(input_list))]
    for i in range(0,len(input_list)):
        word_count = sum(sentence[i].values())
        for term in sentence[i].keys():
            #### populating 2D vector for clustering ####
            j = word_list.index(term)
            term_weight = (math.log(float(line_count)/ngram_dict[term])) * (float(sentence[i][term])/word_count)
            vector_list[i][j] = term_weight
            #temp =  temp +  math.log(line_count)- math.log(ngram_dict[term]) + (math.log(sentence[i][term]) - math.log(word_count))
            temp = temp * (math.log(float(line_count)/ngram_dict[term])) * (float(sentence[i][term])/word_count)
        weight_list.append(temp)
    kmeans = KMeans(n_clusters=cluster_no)
    kmeans.fit_predict(vector_list)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    #print("labels : ",labels)
    for itr in range(0,len(labels)):
        cluster = labels[itr]
        if weight_list[itr] > cluster_dict[cluster]["wt"]:
            cluster_dict[cluster]["wt"] = weight_list[itr]
            cluster_dict[cluster]["ind"] = itr
        
            
    
def term_selection(ngram,line,line_no):
    global ngram_dict,sentence
    ngram_list = list(ngrams(line.split(), ngram))
    sentence[line_no]={}
    for term in ngram_list:
        if term not in sentence[line_no].keys():
            sentence[line_no][term] = 1
        else:
            sentence[line_no][term] = sentence[line_no][term] + 1
        if term not in ngram_dict.keys():
            ngram_dict[term] = 1
        else:
            ngram_dict[term] = ngram_dict[term]+1

def main():
    global input_list,ngram_dict,line_count,sentence,weight_list,cluster_no,cluster_dict
    inp=open(argv[1],"r",encoding="utf8")
    target=open("method3_output.txt","w",encoding="utf8")
    input_list = inp.read().strip('\n').split('.')
    input_list.remove('')
    #input_list.remove('\n')
    line_count = len(input_list)
    #for ngram in range(1,3):
    ngram=int(argv[2])
    cluster_no=int(argv[3])
    for i in range(0,cluster_no):
        cluster_dict[i] = {"ind":0,"wt":0}
    ngram_dict={}
    sentence={}
    weight_list=[]
    vector_list=[[]]
    word_list=[]
    for line in range(0,len(input_list)):
        term_selection(ngram,input_list[line],line)
    sentence_weight()
    final = ""
    for i in range(0,cluster_no):
        final += input_list[cluster_dict[i]["ind"]]+"\n"
    target.write(final)
    inp.close()
    target.close()




if __name__ == "__main__":
    main()
