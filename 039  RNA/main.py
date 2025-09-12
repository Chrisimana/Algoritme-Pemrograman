import sys
print(".:: Program Transkripsi RNA ::.")

dna = input("masukkan string DNA : ")
dna = dna.upper()
rna = ""
for x in dna:
    if(x == 'G'):
        rna += 'C'
    elif(x == 'C'):
        rna += 'G'
    elif(x == 'T'):
        rna += 'A'
    elif(x == 'A'):
        rna += 'U'
    else:
        sys.exit("Bukan DNA !")
        break;

print(f"string RNA : {rna}")
