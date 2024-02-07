def strip_punctuation(string_to_remove_punctuation):
    """
    Remove punctuation characters from a string.
    """
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    punctuation_removed = string_to_remove_punctuation.strip()
    for char in string_to_remove_punctuation:
        if char in punctuation_chars:
            punctuation_removed = punctuation_removed.replace(char, '')
    return punctuation_removed


def get_pos(text_to_count):
    """
    Count the occurrences of positive words in a text string.
    """
    positive_words = []
    with open("positive_words.txt", encoding="utf-8") as pos_f:
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


def get_neg(text_to_count):
    """
    Count the occurrences of negative words in a text string.
    """
    negative_words = []
    with open("negative_words.txt", encoding="utf-8") as neg_f:
        for lin in neg_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    punctuation_stripped_text = strip_punctuation(text_to_count.lower())
    negative_count = 0
    punctuation_stripped_word_list = punctuation_stripped_text.split()
    for word in punctuation_stripped_word_list:
        if word in negative_words:
            negative_count += 1
    return negative_count


def main():
    """
    Analyze sentiment of Twitter data and write results to CSV.
    """
    with open("project_twitter_data.csv", encoding="utf-8") as read_file, open("resulting_data.csv", 'w', encoding="utf-8") as write_file:
        next(read_file)
        write_file.write("Tweet Text,Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n")
        for line in read_file:
            splitted_columns = line.strip().split(",")
            if len(splitted_columns) == 3:
                tweet_text = splitted_columns[0]
                retweet_count = splitted_columns[1]
                reply_count = splitted_columns[2]

                positive_count = get_pos(tweet_text)
                negative_count = get_neg(tweet_text)
                net_score = positive_count - negative_count

                write_file.write(f"{retweet_count},{reply_count},{positive_count},{negative_count},{net_score}\n")
                print("Succeeded in writing the required data to resulting_data.csv")
                
if __name__ == "__main__":
    main()
