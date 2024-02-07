from sentiment_classifier_1 import *

def get_neg(text_to_count):
    negative_words = []
    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    punctuation_stripped_text = strip_punctuation(text_to_count.lower())
    negative_count = 0
    punctuation_stripped_word_list = punctuation_stripped_text.split()
    for word in punctuation_stripped_word_list:
        if word in negative_words:
            negative_count += 1
    return negative_count
