input_string = input("Enter a string: ")
char_frequency = {}
for char in input_string:
    if char != ' ':
        char_frequency[char] = char_frequency.get(char, 0) + 1
print("Character frequency:")
for char, count in char_frequency.items():
    print(f"{char}: {count}")
