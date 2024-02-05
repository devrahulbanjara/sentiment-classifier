def find_longest_word(file_path):
    try:
        with open(file_path, 'r') as file:
            longest_word = ''
            shortest_word = None
            equal_length_words = []
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) > len(longest_word):
                        longest_word = word
                    if shortest_word is None or len(word) < len(shortest_word):
                        shortest_word = word
                    elif len(word) == len(shortest_word):
                        equal_length_words.append(word)
            print(f"Longest Word: {longest_word}")
            print(f"Shortest Word: {shortest_word}")
            print(f"Equal Length Words: {', '.join(equal_length_words)}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
find_longest_word("3.txt")
