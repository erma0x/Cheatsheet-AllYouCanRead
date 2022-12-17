
from DNA_translator import DNA_translator as converter

def switch_values_and_keys(my_dict):
    """
    Swap keys with values in my_dict
    """
    flipped_dict = dict(zip(my_dict.values(), my_dict.keys()))
    return flipped_dict


def encode(DNA):
    """
        convert a string with values 
        of the dictionary "converter"
        return list of bits encoded
    """
    DNA = str(DNA)
    switch = switch_values_and_keys(converter)
    list_ = []
    for w in range(len(DNA)):
        for i in switch.keys():
            if DNA[w] == i :
                list_.append(switch[i])

    return(list_)

def decode(DNA_encoded):
    """
        convert a string with values 
        of the dictionary "converter"
        return list of char decoded
    """
    genome=DNA_encoded
    list_ = []
    for w in range(len(genome)):
        for i in converter.keys():
            if genome[w] == i :
                list_.append(converter[i])

    return(list_)


genome = encode('(a > b)')
decoded = decode(genome)

print(' '.join(genome))
print(''.join(decoded))
