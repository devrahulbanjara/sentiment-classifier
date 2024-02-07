from sentiment_classifier_1 import *


def get_pos(text_to_count_positive):
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    text = strip_punctuation(text_to_count_positive.lower())
    positive_count = 0
    words = text.split()
    for word in words:
        if word in positive_words:
            positive_count += 1
    return positive_count

