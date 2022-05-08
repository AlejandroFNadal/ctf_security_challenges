import sys
args = sys.argv

# command line interface that accepts the following parameters, p, q, exponent, and message
if len(args) != 5:
    print("Usage: python3 plaintext_to_crypt.py p q exponent message")
    sys.exit(1)
else:
    p = int(args[1])
    q = int(args[2])
    exponent = int(args[3])
    message = args[4]

print(f"Original message {message}")
message_hex = [hex(ord(elem))[2:] for elem in message]
print(f"Hex representation of message {message_hex}")
concat_hex_string = ''.join(message_hex)
print(f"Concatenated hex string {concat_hex_string}")
print(concat_hex_string)
int_message = int(concat_hex_string, 16)
print(f"Integer representation of message {int_message}")
print(int_message)
n = p * q
phi = (p-1) * (q-1)
enc = pow(int_message, exponent,n)
print(f"Encrypted message {enc}")


