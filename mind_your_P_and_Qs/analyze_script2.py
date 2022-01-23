from pwn import *
import struct
file = open('values', 'r')
file.readline()
line1 = file.readline()
c = int(line1[3:], 16)
print('c: ',c)
line2 =  file.readline()
n = int(line2[3:], 16)
line3 = file.readline()
e = int(line3[3:],16)

print('n: ',n)
print('e: ',e)
possible_d = 45959976756867064188461878313456131095594928870024290560734980544279642672770319298419938753633600

p1 = 4187733769
q1 = 10974904161315936235592763060991950285574226480683186805564535550620760254200389568714987
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

d = modinv(e,phi)
print('inverse modulus ',d)

result = c**d % n

print('result ',result)

