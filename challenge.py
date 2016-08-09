#!/usr/bin/python
#############THIS CODE TRANSLATES TWO DNA SEQS INTO PROTEINS, COMPARES THEM AND CALCULATES dS/dN RATIO####################

import sys
import os
import numpy
from Bio.Seq import translate



f = open("GrantExcercise.fasta", "r+")

#########################TRANSLATION#####################

seqs={}

for line in f:
    line = line.rstrip()
    if line[0] == ">":
        name = line[1:]
        seqs[name]= ""
    else:
        seqs[name] = seqs[name]+line


f.close

prot_seqs={}

for name,seq in seqs.items():
    aa_seq = translate(seq)
    #print aa_seq
    prot_seqs[name]=aa_seq

    
######################DIFFERENCES IN PROTEIN###############


changes_aa = 0
l=0

for name1,prot1 in prot_seqs.items()[l:]:
	for name2,prot2 in  prot_seqs.items()[l+1:]:
		#print prot1
		#print prot2
		i=0
		while min(len(prot1),len(prot2)) > i:
    			if prot1[i]!=prot2[i]:
				#print prot1[i], prot2[i]
       				print ("In pos %s '%s' has '%s' and '%s' has '%s'"%(i+1,name1, prot1[i], name2, prot2[i]))
    				i+=1
      				changes_aa +=1
			else:
				i+=1
       				continue
print ("There are in total %s aa changes" % (changes_aa))
	
################dS/dN ratio################

changes_N = 0
l=0

for name1,seq1 in seqs.items()[l:]:
	for name2,seq2 in  seqs.items()[l+1:]:
		#print seq1
		#print seq2
		i=0
		while min(len(seq1),len(seq2)) > i:
    			if seq1[i]!=seq2[i]:
				#print seq1[i], seq2[i]
       				#print ("In pos %s '%s' has '%s' and '%s' has '%s'"%(i+1,name1, seq1[i], name2, seq2[i]))
    				i+=1
      				changes_N +=1
			else:
				i+=1
       				continue

print ("There are in total %s nucleotide changes" % (changes_N))

ratio = round(float(changes_N-changes_aa)/changes_N, 3)
print ("dS/dN = %s"%(ratio))

sys.exit()


