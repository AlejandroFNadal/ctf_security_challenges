import sys

p,q,e,crypt = [int(elem) for elem in sys.argv[1:]]

print("Encrypted message:", crypt)
phi = (p-1)*(q-1)

modinv = pow(e,-1,phi)
print("The inverse modulus is ", modinv)
n = p*q
plain = pow(crypt, modinv, n)
plain_hex = hex(plain)[2:]
# We might need to pad the hex
if len(plain_hex) % 2 == 1:
    plain_hex = "0" + plain_hex

plain_str_bytes = bytes.fromhex(plain_hex)
print(plain_str_bytes)
decoded_plain = plain_str_bytes.decode('utf-8')
print(f"The plaintext is {decoded_plain}")

