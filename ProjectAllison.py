import re
codon = []
rcodon = []

#open file and assign to a variable 
f = open("C:/Users/Allison Derry/Documents/OBU Computing 2/hsv-1 genome sequence.txt", "r")
#read the file into a variable
dataset = f.read()
#remove digits from dataset
dataset = re.sub('[0-9]', "", dataset)
# remove //
dataset = re.sub('//', "", dataset)
#remove origin
dataset = re.sub('ORIGIN', "", dataset)
#remove new lines
dataset = re.sub('\n', "", dataset)
#remove spaces
dataset = re.sub(' ',"", dataset)
#locate start codons
startcodon=0
n=0
while(n < 1):
	startcodon=dataset.find("atg", startcodon, len(dataset)-startcodon)
	#locate stop codons
	taacodon=dataset.find("taa", startcodon+3, len(dataset)-startcodon)
	tagcodon=dataset.find("tag", startcodon+3, len(dataset)-startcodon)
	tgacodon=dataset.find("tga", startcodon+3, len(dataset)-startcodon)
	if(taacodon<tagcodon):
		if(taacodon<tgacodon):
			stopcodon=taacodon
			#print("taacodon", startcodon)
		else:
			stopcodon=tgacodon
			#print("tGacodon", startcodon)
	
	elif(tgacodon>tagcodon):
		stopcodon=tagcodon
		#print("taGcodon", startcodon)
	else:
		stopcodon=tgacodon
		#print("tGacodon", startcodon)
	#to add sequences to an array
	codon.append(dataset[startcodon:stopcodon+3])
	if(startcodon > len(dataset) or startcodon < 0):
		n = 2;
	startcodon=stopcodon

#reverse the string and swap the letters
n=0;
while(n < len(codon)):
        rcodon.append (codon[n][len(codon[n])::-1])
        #replace a with u
        rcodon[n] = re.sub('a', "u", rcodon[n])
        #replace t with a
        rcodon[n] = re.sub('t', "a", rcodon[n])
        #replace c with x
        rcodon[n] = re.sub('c', "x", rcodon[n])
        #replace g with c
        rcodon[n] = re.sub('g', "c", rcodon[n])
        #replace x with g
        rcodon[n] = re.sub('x', "g", rcodon[n])
        print("DNA sequence: ", codon[n] ,'\n', "RNA sequence:", rcodon[n])
        n=n+1
answer = 0
print("Total Sequences:  ", len(codon)-3)
while (int(answer) >= 0):
        #str = "Please enter an integer from 0 to " + str(len(dataset)) + " or -1 to quit: "
        answer = int(input("Please enter an sequence you would like to see or -1 to quit:  "))
        if(int(answer) >= 0):
                print("DNA sequence: ", codon[int(answer)] ,'\n', "RNA sequence:", rcodon[int(answer)])
