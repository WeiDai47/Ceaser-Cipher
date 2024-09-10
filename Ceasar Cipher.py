#Here are our list of possible characters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#we imported the random module to save time and this allows our program to choose things at random
import random
#simple print fuction that make our program look more polished for the user
print("Welcome to the Password Generator!")
#input section where the user types in the desired number of letters, symbols, and numbers
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#password variable that will be added to later
password=""
#for statements that choose random characters based on what the user entered prior and adds it to our password variable
for char in range(1, nr_letters+1):
 password+=random.choice(letters)
for sym in range(1, nr_symbols+1):
    password+=random.choice(symbols)
for num in range(1, nr_numbers+1):
    password+=random.choice(numbers)
#this variable is our final password that will be shuffled again
#this makes our password variable into a list for further randomization
finalpassword = list(password)
#this shuffles our password again
random.shuffle(finalpassword)
#here our final password is printed out for the user
print (''.join(finalpassword))
print(f"Your password is : {finalpassword}")
