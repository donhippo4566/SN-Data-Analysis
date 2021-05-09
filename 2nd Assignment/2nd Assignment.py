""" ASSIGNMENT """

#QUESTION 1: String "1000" to integer
int("1000")

#QUESTION 2: Floating point number 3.764 to integer
int(3.764)

print("3.")
#QUESTION 3: Writing "$99.45 dollars"
print("$"+str(99.45),"dollars")

#QUESTION 4: What is type function?
""" the type() function is an in-built function that returns the type of the
    object. eg; list, float, string, tuple, etc.
     """

#QUESTION 5: What are boolean is
""" The boolean is a built-in data type used to represent the truth 
    value of a statement. 
    It makes use of the 'not', 'and', 'or' operators in statements """

#QUESTION 6: Technical name of % operator
""" Modulus, eg x%y (remainder of x/y) """

print()
print("7.")
#QUESTION 7: Declaring a fancy_name
fancy_name = "Winfred Mottey"
print(fancy_name)

print()
print("8.")
#QUESTION 8: Converting hours to seconds
hr = input("Enter hours: ")
sec = 3600 * int(hr)
print(hr,"hours is",sec,"seconds")

print()
print("9.")
# QUESTION 9:
    # Return 100
def easy_money():
    a = 100
    print(a)
easy_money()

print()
    # Return Sushi
def best_food_ever():
    a = "Sushi"
    print(a)
best_food_ever()

    # Add the dollar sign to the value
def convert_to_currency(X):
    print("$"+X)
convert_to_currency(input("X? "))

print()
print("10.")
#QUESTION 10: Return two strings a and b
def string_adder(a, b):
    print(a,b)
string_adder(a = input("a? "), b = input("b? "))

print()
print("11.")
#QUESTION 11: Check if the word has more than 7 letters
def long_word(word):
    w = len(word)
    print(w > 7)
long_word(input("Enter word: "))

print()
print("12.")
#QUESTION 12: Check if the first and last letters are the same
def same_first_and_last_letter():
    a = input("Enter word: ")
    print(a[0] == a[-1])
same_first_and_last_letter()

print()
print("13.")
#QUESTION 13: Display first three letters of word
def first_three_character ():
    a = input("Enter word: ")
    print(a[0]+a[1]+a[2])
first_three_character()