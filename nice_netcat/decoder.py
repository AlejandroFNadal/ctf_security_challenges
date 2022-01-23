# read every line from a file passed as a parameter
import sys

input_file = open(sys.argv[1], 'r')
result_list = []
for line in input_file.readlines():
    result_list.append(chr(int(line)))

temp_str = str(result_list).replace(',','')
temp_str = temp_str.replace('\'', '')
temp_str = temp_str.replace(' ', '')
print(temp_str)