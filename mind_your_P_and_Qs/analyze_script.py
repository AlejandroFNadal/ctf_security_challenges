from pwn import *
import struct
file = open('values', 'r')
file.readline()
line1 = file.readline()
c = int(line1[3:], 10)
print('c: ',c)
line2 =  file.readline()
n = int(line2[3:], 10)
line3 = file.readline()
e = int(line3[3:],10)

print('n: ',n)
print('e: ',e)

p1 = 2434792384523484381583634042478415057961
q1 = 650809615742055581459820253356987396346063
print(p1*q1 == n)

phi = (p1-1)*(q1-1)

print('phi obtained as p-1 * q-1: ',phi)

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

d = modinv(e, phi)
print('inverse modulus ',d)

result = pow(c,d,n)

hex_result = hex(result)

bytes_result = bytes.fromhex(hex_result[2:])


print(bytes_result.decode('ascii'))

