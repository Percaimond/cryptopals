import binascii

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"

raw = binascii.unhexlify(string1)#ok
raw2 = binascii.unhexlify(string2)
a_list = bytes([_a ^ _b for _a, _b in zip(raw,raw2)])
b_list = binascii.hexlify(a_list)
print(b_list)

