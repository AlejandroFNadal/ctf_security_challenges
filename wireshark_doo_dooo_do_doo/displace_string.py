# this function receives a string and adds to the ordinal value of each character a certain value

def displace_string(string, number):
    new_string = ""
    for letter in string:
        # if current letter is a to m 
        if ord(letter) in range(97, 110):
            new_string += chr(ord(letter) + number)
        # if current letter is greater than m, substract the number
        elif ord(letter) in range(110, 123):
            new_string += chr(ord(letter) - number)
        else:
            new_string += letter
    return new_string

# run main, receive a string, the number and run displace string
def main():
    string = input("Enter a string: ")
    number = int(input("Enter a number: "))
    print(displace_string(string, number))

main()