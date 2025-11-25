sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len) if words else ""
print("The longest word is:", longest_word)

def remove_duplicates(s):
    result = ""
    seen = set()
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result

input_string = input("Enter a string: ")

output_string = remove_duplicates(input_string)

print("String after removing duplicates:", output_string)