#identify bad characters to be removed from input
bad_chars = [' ','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','\n', '\t']
#ask for initial input and convert to lowercase
dna = str(input("please enter your DNA sequence in one line \n")).lower()
#create a loop to keep asking for input until they type 'end'
while dna != "end":
    for y in bad_chars :
        dna = dna.replace(y, '') #delete the bad characters
    print("input: \n", dna) #repeat the input with the changes made
    
    replication = dna.maketrans("tcga", "agct") #switch a&t and c&g
    print("Your complimentary sequence is shown below: \n", dna.translate(replication))
    #display complimentary strand
    answer = dna.translate(replication) #define complimentary strand
    transcription = answer.maketrans("tcga", "ucga") #change t to u
    print("The RNA sequence is shown below: \n", answer.translate(transcription))
    #show the transcribed sequence
    mRNA = answer.translate(transcription) #define transcribed sequence
    n = 3 #count by 3
    codons = [mRNA[i:i+n] for i in range (0, len(mRNA), n)] 
    #separate into 3 letter sequences called codons for the length of the mRNA

    protein = {"uuu" : "Phe-", "cuu" : "Leu-", "auu" : "Ile-", "guu" : "Val-",
               "uuc" : "Phe-", "cuc" : "Leu-", "auc" : "Ile-", "guc" : "Val-",
               "uua" : "Leu-", "cua" : "Leu-", "aua" : "Ile-", "gua" : "Val-",
               "uug" : "Leu-", "cug" : "Leu-", "aug" : "Met-", "gug" : "Val-",
               "ucu" : "Ser-", "ccu" : "Pro-", "acu" : "Thr-", "gcu" : "Ala-",
               "ucc" : "Ser-", "ccc" : "Pro-", "acc" : "Thr-", "gcc" : "Ala-",
               "uca" : "Ser-", "cca" : "Pro-", "aca" : "Thr-", "gca" : "Ala-",
               "ucg" : "Ser-", "ccg" : "Pro-", "acg" : "Thr-", "gcg" : "Ala-",
               "uau" : "Tyr-", "cau" : "His-", "aau" : "Asn-", "gau" : "Asp-",
               "uac" : "Tyr-", "cac" : "His-", "aac" : "Asn-", "gac" : "Asp-",
               "uaa" : "STOP \n", "caa" : "Gin-", "aaa" : "Lys-", "gaa" : "Glu-",
               "uag" : "STOP \n", "cag" : "Gin-", "aag" : "Lys-", "gag" : "Glu-",
               "ugu" : "Cys-", "cgu" : "Arg-", "agu" : "Ser-", "ggu" : "Gly-",
               "ugc" : "Cys-", "cgc" : "Arg-", "agc" : "Ser-", "ggc" : "Gly-",
               "uga" : "STOP \n", "cga" : "Arg-", "aga" : "Arg-", "gga" : "Gly-",
               "ugg" : "Trp-", "cgg" : "Arg-", "agg" : "Arg-", "ggg" : "Gly-" 
               }
    protein_sequence = ""
    #convert codons to amino acids called protein sequence, create new lines
    #after stop condons
    
    for x in codons:
        if x in protein:
            protein_sequence += protein[x]
        else:
            protein_sequence += x
    print("translation: ", protein_sequence) #display amino acid sequnces
    #ask for input and show how to quit the program
    dna = str(input("please enter your DNA sequence in one line or 'end' to quit \n")).lower()
    if dna == "end":
        print ("thank you :)")
    #end program and print thank you when 'end' is entered
