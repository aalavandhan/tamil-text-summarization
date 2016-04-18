import sys
import editdistance

if __name__ == "__main__":

	filePath=sys.argv[1]
	number=sys.argv[2]

	fileObj=open(filePath,"r")
	word_dict={}
	total_words=0

	for line in fileObj.read().split("."):
		for word in line.split():
			total_words=total_words+1
			word_dict.setdefault(word,0)
			word_dict[word]=word_dict[word]+1

	fileObj.close()
	sentence_weight_dict={}
	sentence_no=0
	sentence_length={}
	line_dict={}
	fileObj=open(filePath,"r")
	for line in fileObj.read().split("."):
		line.strip("\n")

		if len(line) != 0:
			sentence_no=sentence_no+1
			sentence_weight_dict.setdefault(sentence_no,0)
			sentence_length.setdefault(sentence_no,0)
			# line.setdefault(sentence_no,"")
			line_dict[sentence_no]=line
			for word in line.split():
				sentence_length[sentence_no]=sentence_length[sentence_no] + 1
				affinity_weight=((word_dict[word]-1)/float(total_words))
				sentence_weight_dict[sentence_no]=sentence_weight_dict[sentence_no]+ affinity_weight

	fileObj.close()

	# lsw_dict={}
	vertex_weight={}
	for key in sentence_weight_dict.keys():
		vertex_weight.setdefault(key,0)
		# lsw_dict.setdefault(key,{})
		for sentence_no in sentence_weight_dict.keys():
			if key != sentence_no:
				vertex_weight[key]=vertex_weight[key] + ((max(sentence_length[key],sentence_length[sentence_no]) - editdistance.eval(line_dict[key].split(),line_dict[sentence_no].split()))/ float(max(sentence_length[key],sentence_length[sentence_no])))



	rank={}
	for key in sentence_weight_dict.keys():
		rank.setdefault(key,0)
		rank[key]=(sentence_weight_dict[key]+vertex_weight[key])/float(2)


	output_fileObj=open("output_method1","w")


	for line_no in sorted(rank, key=rank.get, reverse=True)[1:int(number)+1]:
		output_fileObj.write(str(line_dict[line_no]).strip()+".")


  	output_fileObj.close()
