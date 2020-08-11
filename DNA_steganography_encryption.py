#!/usr/bin/env python3

import random


message = str(input("Enter your message : "))

dna_key = { "A" : "00" ,
    "C" : "01" ,
    "G" : "10" ,
    "T" : "11"
    }


# Generate random DNA.
def randomDna(len_dna):
    nucleotides = ["A", "T", "G", "C"]
    input_dna = "".join([random.choice(nucleotides)for nt in range(len_dna)])
    return input_dna


# Converting our message into binary.
def msg_to_bin(message):
    message_ascii_bin_list = []
    for nt in message:
        message_ascii = ord(nt)
        message_ascii_bin_temp = bin(message_ascii)
        message_ascii_bin = message_ascii_bin_temp[0] + message_ascii_bin_temp[2:]  # the 'b' at index [1] has been eliminated.
        message_ascii_bin_list.append(message_ascii_bin)
    message_ascii_bin_string = "".join(i for i in message_ascii_bin_list)
    return message_ascii_bin_string


# Converting DNA to binary
def dna_to_bin(dna):
    dna_ascii_bin_list = []
    for nt in dna:
        dna_ascii_bin_list.append(dna_key[nt])
    dna_ascii_bin_string = "".join(i for i in dna_ascii_bin_list)
    return dna_ascii_bin_string




# Converting our message into binary.
message_bin = msg_to_bin(message)
#print("message binary", message_bin)
#print(len(message_bin))
len_message_bin = len(message_bin)
len_random_dna = int((3*len_message_bin)/2)
# Generate random DNA of appropriate length
random_dna = randomDna(len_random_dna)
#print("Random dna : ", random_dna)
#print(len(random_dna))
# Converting random DNA to binary
dna_bin = dna_to_bin(random_dna)
#print("DNA biunary", dna_bin)
#print(len(dna_bin))





# Merging message in dna
def merging(message_bin, dna_bin):
    msg_part = [message_bin[i] for i in range(len(message_bin))]
    dna_part = [dna_bin[i:i+3] for i in range(0, len(dna_bin), 3)]
    encoded_dna_bin_list = []

    for i in range(len(msg_part)):
        encoded_dna_bin_temp = msg_part[i] + dna_part[i]
        encoded_dna_bin_list.append(encoded_dna_bin_temp)
    encoded_dna_bin = "".join(encoded_dna_bin_list)
    return encoded_dna_bin


# This is the final encoded DNA, formed by merging message with starting DNA.
encoded_dna_bin_final = merging(message_bin, dna_bin)
#print("Encoded DNA (binary) is : {}".format(encoded_dna_bin_final))
#print(len(encoded_dna_bin_final))


# NOW WE WILL CONVERT THIS ENCODED DNA, WHICH IS IN BINARY FORM
# TO DNA IN [A, C, G, T] FORM.

encoded_dna_list = []
for i in range(0, len(encoded_dna_bin_final), 2):
    nt = encoded_dna_bin_final[i:i+2]
    if nt == "00" :
        encoded_dna_list.append("A")
    elif nt == "01":
        encoded_dna_list.append("C")
    elif nt == "10":
        encoded_dna_list.append("G")
    elif nt == "11":
        encoded_dna_list.append("T")

encoded_dna = "".join(encoded_dna_list)

print("Encoded DNA: ", encoded_dna)


# Copying the encoded DNA into a filr name as "Encoded_DNA.txt"
file = open("Encoded_DNA.txt", "x")
file.write(encoded_dna)
