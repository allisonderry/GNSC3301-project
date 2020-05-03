bad_chars = [' ','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','\n', '\t']
dna = str(input("please enter your DNA sequence \n")).lower()
while dna != "end":
    for y in bad_chars :
        dna = dna.replace(y, '')
    print("input: \n", dna)
    
    replication = dna.maketrans("tcga", "agct")
    print("Your complimentary sequence is shown below: \n", dna.translate(replication))
    answer = dna.translate(replication)
    transcription = answer.maketrans("tcga", "ucga")
    print("The RNA sequence is shown below: \n", answer.translate(transcription))
    mRNA = answer.translate(transcription)
    n = 3
    codons = [mRNA[i:i+n] for i in range (0, len(mRNA), n)]


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
               "uaa" : "STOP", "caa" : "Gin-", "aaa" : "Lys-", "gaa" : "Glu-",
               "uag" : "STOP", "cag" : "Gin-", "aag" : "Lys-", "gag" : "Glu-",
               "ugu" : "Cys-", "cgu" : "Arg-", "agu" : "Ser-", "ggu" : "Gly-",
               "ugc" : "Cys-", "cgc" : "Arg-", "agc" : "Ser-", "ggc" : "Gly-",
               "uga" : "STOP", "cga" : "Arg-", "aga" : "Arg-", "gga" : "Gly-",
               "ugg" : "Trp-", "cgg" : "Arg-", "agg" : "Arg-", "ggg" : "Gly-" 
               }
    protein_sequence = ""

    for x in codons:
        if x in protein:
            protein_sequence += protein[x]
        else:
            protein_sequence += x
    print("translation: ", protein_sequence)
    dna = str(input("please enter your DNA sequence or 'end' to quit \n")).lower()
    if dna == "end":
        print ("thank you.")
