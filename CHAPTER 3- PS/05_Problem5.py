letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Honey").replace("<|Date|>", "24 December 2026"))

#chaining of replace function is used to replace multiple values in the string.