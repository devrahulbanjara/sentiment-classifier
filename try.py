equal = {3: ["abc"], 4: ["abcd"]}
word = "def"
if len(word) in equal:
    equal[len(word)].append(word)
else:
    equal[len(word)] = [word]

print(equal)
