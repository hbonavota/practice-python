#SOLOLEARN -- Python for Beginners ---
#Strings

#The man, the legend, Steve Jobs said a lot of cool stuff. Write a program to output his most famous quote in the following format:
#"Stay hungry, stay foolish" by Steve Jobs

print("\"Stay hungry, stay foolish\" by Steve Jobs")

#Newlines

#This code tries to make a triangle out of stars. But oh no! There’s an error in there somewhere-it outputs all the stars on one line, instead of separate lines.

print("*\n**\n***\n****")

#String Operations
#You’re given a task to write the word "hi" 42 times. Boring, right?

#Let’s write a program to do it for you.

#Create a program to output "hi" 42 times, without any separators, on the same line.

print(42 * "hi")

#You need to make a program for a leaderboard.
#The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
#1.
#2.
#3.

print("""
1.
2.
3.
4.
5.
6.
7.
8.
9.
""")

#Variables

#You’re making a contact management system.

#The given program declares two variables, name and age.

#Complete the code to output "name is age years old", where name and age are the declared variable values.
name = "James"
age = "42"
print (name+" is "+age+" years old")

#Taking User Input


#You’re working on a notification system and need to make the notification text eye-catching.

#Write a program that takes the text as input and outputs it by adding 3 stars at the beginning and the end.

name = input()
print("***"+ " "+name +" "+"***")


name = input()
age = input()


#Working with Input


#Now that we know how to take user input, let's improve our contact card program that we previously made using variables.

#Change the given code to take the name and age from user input and use them in the output.
print(name + " is "+age+" years old")

#Tip Calculator


#When you go out to eat, you always tip 20% of the bill amount. But who’s got the time to calculate the right tip amount every time? Not you that’s for sure! You’re making a program to calculate tips and save some time.

#Your program needs to take the bill amount as input and output the tip as a float.

bill = int( input() )
#tu código va aquí
print(bill*20/100)

