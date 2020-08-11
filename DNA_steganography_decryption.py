#!/usr/bin/env python3


# Converting DNA to binary
dna_key = { "A" : "00" ,
    "C" : "01" ,
    "G" : "10" ,
    "T" : "11"
    }

def dna_to_bin(dna):
    dna_ascii_bin_list = []
    for nt in dna:
        dna_ascii_bin_list.append(dna_key[nt])
    dna_ascii_bin_string = "".join(i for i in dna_ascii_bin_list)
    return dna_ascii_bin_string


encoded_dna_file = open("Encoded_DNA.txt", "r")
encoded_dna = encoded_dna_file.readlines()
#print("encoded dna : ", encoded_dna)
#print(type(encoded_dna))

encoded_dna_bin = dna_to_bin(encoded_dna[0])

#print("encoded dna binary : ", encoded_dna_bin)


# Extract message (in binary) from encoded_dna_bin.
message_bin_list = []
for i in range(0, len(encoded_dna_bin), 4):
    message_bin_list.append(encoded_dna_bin[i])
message_bin =  "".join(str(i) for i in message_bin_list)

#print("message bin : " , message_bin)

# Now, we convert these characters from binary to ascii and then in alphabet.
message_chr_binlist = []

for i in range(0,len(message_bin), 8):
    message_chr_binlist.append(message_bin[i:i+8])
#print(message_chr_binlist)

# Decrypting message bin list word by word.
decrypt_message_list = []
for i in message_chr_binlist:
    decode_ascii = int(str(i), 2)
    decode_chr = chr(decode_ascii)
    decrypt_message_list.append(decode_chr)
decrypted_message = "".join(decrypt_message_list)

# Printing the secret message.
print("The secret message is : {}".format(decrypted_message))

# Putting the secret message in a txt file.
file = open("Message.txt", "x")
file.write(decrypted_message)
file.close()
