with open("3.txt", 'r') as file:
    longest = ''
    shortest = None
    equal = {}

    for line in file:
        words = line.split()
        for word in words:
            if len(word) > len(longest):
                longest = word
            if shortest is None or len(word) < len(shortest):
                shortest = word
            if len(word) in equal:
                equal[len(word)].append(word)
            else:
                equal[len(word)] = [word]

    print(f"The longest word in the file is: {longest}")
    print(f"The shortest word in the file is: {shortest}")
    for length, words in equal.items():
        if len(words) > 1:
            print(f"Words with length {length}: {words}")