str1 = "AbcDEfghIJ"
print(str1.upper())  # Converts to uppercase -> ABCDEFGHIJ

print(str1.lower())  # Converts to lowercase -> abcdefghij

str2 = " Silver Spoon "
print(str2.strip())  # Removes leading and trailing spaces -> Silver Spoon

str3 = "hello!!!"
print(str3.rstrip("!"))  # Removes trailing '!' -> hello

str4="spoon"
print(str4.replace("sp","m"))

str5="jubair islam"
print(str5.split(" ")) # splits the string into a list of words -> ['jubair','islam]'

str6="hello worLD"
print(str6.capitalize()) # Capitalizes the first letter of the string -> Hello world

print(str5.center(50))
print(str5.center(50,"."))
      