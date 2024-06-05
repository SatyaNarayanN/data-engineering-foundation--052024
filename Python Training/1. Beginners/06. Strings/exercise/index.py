single_quoted_string = 'Well done is better than well said.'
double_quoted_string = "Imagination is more important than knowledge. -Albert Einstein"
Multi_quoted_string = '''You should never engage in action for the sake of reward, 
nor should you long for inaction."
-Lord Krishna, Bhagavad Gita'''

print(single_quoted_string)
print(double_quoted_string)
print(Multi_quoted_string)

first_name = "Hello"
last_name = "World"
concatenate = first_name+" "+last_name
print(concatenate)

name = "data_science"
length = len(name)
print(length)

variable = "New Delhi"
first_char = variable[0]
substring = variable[1:3]
print(first_char, substring)

sentence = "   Do Not Expect Anything.   "
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()
print(uppercase_sentence, lowercase_sentence)

string = "   Do Not Expect Anything.   "
stripped_sentence = string.strip()
print(stripped_sentence)

name = "shaun"
age = 25
city = "Hyd"
formatted_string = (f"My name is {name},I am {age} years old and i live in {city}")
print(formatted_string)
