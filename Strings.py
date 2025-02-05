#Strings in Python


text = "Thick brown fox"
print("quick" in text)
print("brown" in text)

#using in for substring checks

#sting slicing

text = "Hello, World"
print(text[7:12])
print(text[::-1])

#Multiline Strings:

multiline_string = """
This is a 
multiline string
in python
"""
print(multiline_string)

#joins Lists into Strings

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)
