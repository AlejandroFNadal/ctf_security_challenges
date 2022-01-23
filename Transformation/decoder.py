import sys
path = sys.argv[1]
input_file = open(path, 'r')

result = ''
flag = input_file.readline()
#Python automatically reads every character as utf16 because of the file structure

for i in range(0, len(flag)):
    elem = flag[i]
    hex_value = hex(ord(elem))
    print(f'Hex value {hex_value}')
    first_byte = hex_value[2:4]
    second_byte = hex_value[4:6]
    result += chr(int(first_byte, 16))
    result += chr(int(second_byte,16))
print(result)



