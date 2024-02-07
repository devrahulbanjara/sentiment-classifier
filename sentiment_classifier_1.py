def strip_punctuation(string_to_remove_punctuation):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    punctuation_removed = string_to_remove_punctuation
    for char in string_to_remove_punctuation:
        if char in punctuation_chars:
            punctuation_removed = punctuation_removed.replace(char, '')
    return punctuation_removed


