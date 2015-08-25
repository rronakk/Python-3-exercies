def word_count(sentence):
    s_lower = sentence.lower()
    list_of_words = s_lower.split()
    word_dict={}
    for ch in list_of_words:
        if ch in word_dict:
            word_dict[ch] = word_dict[ch] + 1
        else:
            word_dict[ch] = 1

    return word_dict
        
    
print(word_count("I AM awesome I really am I really really I"))