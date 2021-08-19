alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def last_first(k, string):
    listed_string = []
    new_listed_string = []
    new_string = ''
    for letter in string:
        listed_string.append(letter)
    listed_string = listed_string[-1:]+listed_string[:-1]
    for element in listed_string:
        if alphabet.index(element) == 25:
            new_listed_string.append('a')
        else:
            next_word = str(alphabet[(alphabet.index(element)) + 1])
            new_listed_string.append(next_word)
    for arg in new_listed_string:
        new_string = new_string+arg
    if k == 1:
        print(new_string)
        return
    else:
        last_first(k-1, new_string)
