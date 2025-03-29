def num_words(contents):
    words = contents.split()
    return len(words)

def letter_count(contents):
    letter_count = {}
    for letter in contents:
        letter = letter.lower()
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def sort_on(dict_list):
        return dict_list["count"]

def sort_letters(count_dict):
    dict_list = [] 
    for key in count_dict:
        dict_list.append({"char": key, "count": count_dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

   
    
    
    
