import string
alphabet = " "+ string.ascii_lowercase 
keys = alphabet
values = range(0,27)
positions = dict(zip(keys, values))
print(positions)




###Q3
##alphabet and positions have already been defined from previous exercises. 
##Use positions to create an encoded message based on message where each character 
##in message has been shifted forward by 1 position, as defined by positions.
## Note that you can ensure the result remains within 0-26 using result % 27

message = "hi my name is caesar"

def caesar(message, key):

    letters = dict(enumerate(alphabet))
    coded_letters = {j: (i + key) % len(alphabet) for i, j in letters.items()}
    coded_message = ''
    for i in message:
        coded_message += letters[coded_letters[i]]
    return coded_message



encoded_message = caesar(message, 1)

print(encoded_message)


##define new dictionary
shift_pos=1
positions_shift={}
positions_shift[keys] = positions.get(keys, 0) + shift_pos


def encode(message,key):
    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string

encoded_message=encode(message,3)
print(encoded_message)

decoded_message = caesar(encoded_message,-3)
print (decoded_message)

