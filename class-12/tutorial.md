String Slicing & Operations on String

Length of a String
We can find the length of a string using len() function.

fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

String as an array
A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

Example:
pie = "ApplePie"
print(pie[:5])
print(pie[6]) #returns character at specified index
Output:
Apple
i
Note: This method of specifying the start and end index to specify a part of a string is called slicing.

Slicing Example:
pie = "ApplePie"
print(pie[:5]) #Slicing from Start
print(pie[5:]) #Slicing till End
print(pie[2:6]) #Slicing in between
print(pie[-8:]) #Slicing using negative index
Output:
Apple
Pie
pleP
ApplePie

The code nm[-4:-2] is using Python's string slicing feature. Here's how it works:

nm = "harry" assigns the string "harry" to the variable nm.
nm[-4:-2] slices the string nm from index -4 to -2.
In Python, negative indices count from the end of the string:

-1 refers to the last character ('y' in this case),
-2 refers to the second-to-last character ('r'),
-3 refers to the third-to-last character ('r'),
-4 refers to the fourth-to-last character ('a')
