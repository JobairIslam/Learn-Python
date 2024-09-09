string method:

Python provides a set of built-in methods that we can use to alter and modify the strings.
upper() :
The upper() method converts a string to upper case.

Example:
str1 = "AbcDEfghIJ"
print(str1.upper())

lower()
The lower() method converts a string to lower case.

Example:
str1 = "AbcDEfghIJ"
print(str1.lower())

strip() :
The strip() method removes any white spaces before and after the string.

Example:
str2 = " Silver Spoon "
print(str2.strip)
Output:
Silver Spoon

rstrip() :
the rstrip() removes any trailing characters. Example:

str3 = "Hello !!!"
print(str3.rstrip("!"))
Output:
Hello

replace() :
The replace() method replaces all occurences of a string with another string. Example:

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
Output:
Silver Moon

split() :
The split() method splits the given string at the specified instance and returns the separated strings as list items.

Example:
str2 = "Silver Spoon"
print(str2.split(" ")) #Splits the string at the whitespace " ".

capitalize() :
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

Example:
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
Output:
Hello
Hello world

center() :
The center() method aligns the string to the center as per the parameters given by the user.

Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50))
Output:
Welcome to the Console!!!

We can also provide padding character. It will fill the rest of the fill characters provided by the user.

Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))
Output:
............Welcome to the Console!!!.............
