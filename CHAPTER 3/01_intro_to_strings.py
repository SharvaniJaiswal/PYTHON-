name="Honey"  
#Strings are a sequence of characters enclosed in single or double quotes.
#Strings are immutable, meaning they cannot be changed after they are created.
nameshort= name[0:3] # starting index is inclusive and ending index is exclusive. It will print the characters from index 0 to 2.
#slicing is used to extract a portion of a string by specifying the start and end indices. The syntax for slicing is string[start:end], where start is the index of the first character to include, and end is the index of the first character to exclude. If start is omitted, it defaults to 0, and if end is omitted, it defaults to the length of the string.
a=len(name)
print("The length of the string is", a)
print("The first three characters of the string are", nameshort)
character1= name[0] # indexing is used to access individual characters in a string by their position. The syntax for indexing is string[index], where index is the position of the character to access. Indexing starts at 0 for the first character, 1 for the second character, and so on. Negative indexing can also be used to access characters from the end of the string, with -1 being the last character, -2 being the second-to-last character, and so on.
character2= name[1]
print("The first character of the string is", character1)
print("The second character of the string is", character2)
#positive slicing and negative slicing can be used to extract portions of a string. Positive slicing uses positive indices to specify the start and end positions, while negative slicing uses negative indices to specify the start and end positions from the end of the string. For example, name[0:3] extracts the first three characters of the string, while name[-3:] extracts the last three characters of the string.
