import re
import sys
import os


from Bio import SeqIO


A_hapl = open("A_hapl.fasta", "w")
B_hapl = open("B_hapl.fasta", "w")

for seq_record in SeqIO.parse("C_alb.fasta", "fasta"):
	name = str(seq_record.id)
	seq = str(seq_record.seq)
    	if re.search(r'.*chr.A.*',name):
		print ("%s%s"%(">",name))
		print ("%s"%(seq[0:100]))
		A_hapl.write("%s%s\n"%(">",name))
		A_hapl.write("%s\n"%(seq))
    	elif re.search(r'.*chr.B.*', name):
		print ("%s%s"%(">",name))
		print ("%s"%(seq[0:100]))
		B_hapl.write("%s%s\n"%(">",name))
		B_hapl.write("%s\n"%(seq))
	else:
		print "No_match"

A_hapl.close()
B_hapl.close()



