def get_num_words(text): 
    words = text.split()
    return len(words)

def get_num_characters(text): 
    dict_characters = {}
    for char in text.lower(): 
        dict_characters[char] = 1 + dict_characters.get(char, 0)
    return dict_characters

def get_sorted_num_characters(dict_char): 
    return sorted(dict_char.items(), key=lambda x: x[1], reverse=True)