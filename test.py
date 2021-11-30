def find_pos(string,word):

    for i in range(len(string) - len(word)+1):
        if string[i:i+len(word)] == word:
            return i
    return 'Not Found'

string = "the dude is a cool dude"
word = 'dude'
print(find_pos(string,word))
# output 4
