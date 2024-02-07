from sentiment_classifier_1 import *


def get_pos(text_to_count):
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    punctuation_stripped_text = strip_punctuation(text_to_count.lower())
    positive_count = 0
    punctuation_stripped_word_list = punctuation_stripped_text.split()
    for word in punctuation_stripped_word_list:
        if word in positive_words:
            positive_count += 1
    return positive_count

