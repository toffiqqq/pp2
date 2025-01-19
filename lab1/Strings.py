print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")



#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

#Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2)
b = "Hello, World!"
print(b[-5:-2])

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#\'	    Single Quote	
#\\ 	Backslash	
#\n  	New Line	
#\r	    Carriage Return	
#\t	    Tab	
#\b	    Backspace	
#\f	    Form Feed	
#\ooo	Octal value	
#\xhh	Hex value
    
#capitalize()	    Converts the first character to upper case
#casefold()	        Converts string into lower case
#center()        	Returns a centered string
#count()        	Returns the number of times a specified value occurs in a string
#encode()        	Returns an encoded version of the string
#endswith()	        Returns true if the string ends with the specified value
#expandtabs()   	Sets the tab size of the string
#find()	            Searches the string for a specified value and returns the position of where it was found
#format()        	Formats specified values in a string
#ormat_map()    	Formats specified values in a string
#index()        	Searches the string for a specified value and returns the position of where it was found
#isalnum()        	Returns True if all characters in the string are alphanumeric
#isalpha()      	Returns True if all characters in the string are in the alphabet
#isascii()      	Returns True if all characters in the string are ascii characters
#sdecimal()     	Returns True if all characters in the string are decimals
#isdigit()   	    Returns True if all characters in the string are digits
#isidentifier()  	Returns True if the string is an identifier
#islower()	        Returns True if all characters in the string are lower case
#isnumeric()    	Returns True if all characters in the string are numeric
#isprintable()   	Returns True if all characters in the string are printable
#isspace()         	Returns True if all characters in the string are whitespaces
#istitle()         	Returns True if the string follows the rules of a title
#isupper()        	Returns True if all characters in the string are upper case
#join()	            Joins the elements of an iterable to the end of the string
#ljust()        	Returns a left justified version of the string
#lower()        	Converts a string into lower case
#lstrip()       	Returns a left trim version of the string
#maketrans()    	Returns a translation table to be used in translations
#partition()    	Returns a tuple where the string is parted into three parts
#replace()       	Returns a string where a specified value is replaced with a specified value
#rfind()	        Searches the string for a specified value and returns the last position of where it was found
#rindex()       	Searches the string for a specified value and returns the last position of where it was found
#rjust()        	Returns a right justified version of the string
#rpartition()   	Returns a tuple where the string is parted into three parts
#rsplit()	        Splits the string at the specified separator, and returns a list
#rstrip()	        Returns a right trim version of the string
#split()	        Splits the string at the specified separator, and returns a list
#splitlines()	    Splits the string at line breaks and returns a list
#startswith()	    Returns true if the string starts with the specified value
#strip()	        Returns a trimmed version of the string
#swapcase()     	Swaps cases, lower case becomes upper case and vice versa
#title()        	Converts the first character of each word to upper case
#translate()    	Returns a translated string
#upper()     	    Converts a string into upper case
#zfill()	        Fills the string with a specified number of 0 values at the beginning