
# coding: utf-8

# In[4]:

#Store the DNA as a string in a variable
myDNA="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"


# In[5]:

#Print to the screen the number of characters in the string stored in the variable myDNA; the return value should be an interger
print(len(myDNA))


# In[97]:

#Convert the DNA sequence to RNA; replace the "T's" with "U's"; first convert the sequence to upper case.
dna_to_rna=myDNA.upper().replace('T','U')
print(dna_to_rna)


# In[98]:

#Start the reverse complement of the RNA sequence. Use the replace method. Need to replace upper case letters with lower case to avoid problems down the road! 
revcomp=dna_to_rna.replace('U','a')
revcomp1=revcomp.replace('A','u')
#By replacing only the capital A's with a lower case t, then this doesn't undo what you did in the first replacement.
revcomp2=revcomp1.replace('C','g')
revcomp3=revcomp2.replace('G','c')
#Reverse the order of the replaced DNA sequence, stored in the variable revcomp3
revcomp4=revcomp3[::-1]
revcomp5=revcomp4.upper()
print(revcomp5)


# In[93]:

#Start the reverse complement of the DNA sequence. Use the replace method. Need to replace upper case letters with lower case to avoid problems down the road! 
#Need to make the DNA sequence upper case first 
myDNA_upper=myDNA.upper()
revcomp_dna=myDNA_upper.replace('T','a')
revcomp1_dna=revcomp_dna.replace('A','t')
#By replacing only the capital A's with a lower case t, then this doesn't undo what you did in the first replacement.
revcomp2_dna=revcomp1_dna.replace('C','g')
revcomp3_dna=revcomp2_dna.replace('G','c')
#Reverse the order of the replaced DNA sequence, stored in the variable revcomp3
revcomp4_dna=revcomp3_dna[::-1]
revcomp5_dna=revcomp4_dna.upper()
print(revcomp5_dna)


# In[96]:

#Extract the substring, 13th and 14th codons of the RNA reverse complement, and print them to the screen. Remember that python starts counting at zero. The first number is inclusive and the last number in the range is exclusive.
print(revcomp5[38:44])
#Extract the substring, 13th and 14th codons of the DNA sequence, and print them to the screen
print(myDNA_upper[38:44])
#Extract the substring, 13th and 14th codons of the RNA sequence, and print them to the screen
print(dna_to_rna[38:44])
#Extract the substring, 13th and 14th codons of the DNA reverse complement, and print them to the screen
print(revcomp5_dna[38:44])


# In[80]:

#Create a dictionary for the codons and their associated amino acid based on the afforementioned file in the assignment text
def translate_nucleotides(sequence,codon_table):
    '''This function translates RNA to protein using a dictionary'''
    #Split the sequence into triplets after determining the length of the sequence
    sequence_length=len(sequence)
    all_codons=[sequence[i:i+3] for i in range(0,sequence_length,3)]
    #Translate (based on the codon table given) and join all of the codons into a string
    protein_sequence=''.join([codon_table[codon] for codon in all_codons])
    return protein_sequence


# In[105]:

#Generate a dictionary based on the translation file for mitrochondria provided in the CompPhyl17 repository
#Key should be the RNA codon, value should be the corresponding amino acid
#Need to account for any part of the sequence that isn't three aminoa acids, ex. AA, AU, GA, etc. Make the value for this an empty space
translation_table_RNA={'UUU':'F','UUC':'F','UUA':'L','UUG':'L','UCU':'S','UCC':'S','UCA':'S','UCG':'S','UAU':'Y','UAC':'Y','UAA':'*','UAG':'*','UGU':'C','UCG':'C','UGA':'W','UGG':'W','CUC':'L','CUU':'L','CUA':'L','CUG':'L','CCU':'P','CCC':'P','CCA':'P','CCG':'P','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'M','AUG':'M','ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K','AGU':'S','AGC':'S','AGA':'*','AGG':'*','GUU':'V','GUC':'V','GUA':'V','GUG':'V','GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E','GGU':'G','GGC':'G','GGA':'G','GGG':'G','A':'','U':'','C':'','G':'','AA':'','AU':'','AC':'','AG':'','UA':'','UU':'','UC':'','UG':'','CC':'','CA':'','CU':'','CG':'','GC':'','GA':'','GU':'','GC':''
    }
translation_table_DNA={'TTT':'F','TTC':'F','TTA':'L','TTG':'L','TCT':'S','TCC':'S','TCA':'S','TCG':'S','TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','TGT':'C','TCG':'C','TGA':'W','TGG':'W','CTC':'L','CTT':'L','CTA':'L','CTG':'L','CCT':'P','CCC':'P','CCA':'P','CCG':'P','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','CGT':'R','CGC':'R','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ATA':'M','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T','AAT':'N','AAC':'N','AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'*','AGG':'*','GTT':'V','GTC':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A','GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G','A':'','T':'','C':'','G':'','AA':'','AT':'','AC':'','AG':'','TA':'','TT':'','TC':'','TG':'','CC':'','CA':'','CT':'','CG':'','GC':'','GA':'','GT':'','GC':''
    }
#Translate the reverse complement of the RNA sequence
translated_RNA_rev=translate_nucleotides(revcomp5,translation_table_RNA)
print('The translation of the reverse complemented RNA sequence is: '+translated_RNA_rev)
#Translate the reverse complement of the DNA sequence
translated_DNA_rev=translate_nucleotides(revcomp5_dna,translation_table_DNA)
print('The translation of the reverse complemented DNA sequence is: '+translated_DNA_rev)
#Translate the RNA sequence
translated_RNA=translate_nucleotides(dna_to_rna,translation_table_RNA)
print('The translation of the RNA sequence is: '+translated_RNA)
#Translate the DNA sequence
translated_DNA=translate_nucleotides(myDNA_upper,translation_table_DNA)
print('The translation of the DNA sequence is: '+translated_DNA)

