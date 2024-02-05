
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open("3.txt", 'w') as file:
    for color in color_list:
        file.write(f"{color}\n")



