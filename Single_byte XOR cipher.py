import binascii

string1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
string2 = "00000000000000000000000000000000000000000000000000000000000000000001"

raw = binascii.unhexlify(string1)
raw2 = binascii.unhexlify(string2)
a_list = bytes([_a ^ _b for _a, _b in zip(raw,raw2)])
b_list = binascii.hexlify(a_list)
print(b_list)
print(a_list)
