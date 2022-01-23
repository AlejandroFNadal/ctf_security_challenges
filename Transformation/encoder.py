string = 'Hola'

first_part = ord(string[0])
print(f'First byte {first_part}')
first_part_shifted = first_part << 8
print(f'First byte shifted {first_part_shifted}')
second_part = ord(string[1])
print(f'Second part {second_part}')

added_elements = first_part_shifted + second_part
print(f'added_elements = {added_elements}')
first_two_letters = chr(added_elements)
print(f'First two letters: {first_two_letters}')

result = ''.join([chr((ord(string [i]) << 8) + ord(string[i+1])) for i in range(0, len(string),2)])
print(result)


for elem in result:
    print(ord(elem))
    elem_in_hex = hex(ord(elem))[2:]
    first_byte = elem_in_hex[0:2]
    print(chr(int(first_byte, 16)))
    

