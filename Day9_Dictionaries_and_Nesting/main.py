#Dictionaries & Nesting
programming_dictionary = {
 "Bug": "An error in a program that prevents the program from running as expected.",
 "Function": "A piece of code that you can easily call over and over again.",
 "Loop": "The action of doing something over and over again."
}

#Retrieving items from dictionary
#print(programming_dictionary["Bug"])

#Adding new entry
programming_dictionary["Iteration"] = "A piece of code run in a for / while loop"
#print(programming_dictionary["Iteration"])

#Create an empty dictionary / Wipe an existing dictionary
#empty_dictionary = {}

#Edit item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

#Loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
