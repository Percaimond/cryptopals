import base64
import binascii

string = input("Plese insert the String: ")
raw = binascii.unhexlify(string)
bin_raw = base64.b64encode(raw)
print(bin_raw)