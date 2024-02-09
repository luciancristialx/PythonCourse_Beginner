import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers =int(input("How many numbers would you like in your password?\n"))

pwd = ""
total_length = nr_letters + nr_symbols + nr_numbers
mylist = [letters,numbers,symbols]

for number in range(1, total_length+1):
  listIndex = random.randint(0,2)
  if listIndex == 0:
      characterIndex = random.randint(0,len(letters)-1)
  elif listIndex == 1:
      characterIndex = random.randint(0, len(numbers)-1)
  else:
      characterIndex = random.randint(0, len(symbols)-1)
  character = mylist[listIndex][characterIndex]
  pwd+=character
print(pwd)

#random.choice; random.shuffle