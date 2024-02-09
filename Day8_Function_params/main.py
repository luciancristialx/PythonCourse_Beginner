#Simple Function
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
# greet()

#Function with single parameter
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
# greet_with_name("Lucian")

#Function with multiple parameters
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
# greet_with("Lucian", "Romania") #Positional arguments
# greet_with(name = "Dragos", location = "Madagascar") #Keyword arguments

#Prime Number
def prime_checker(number):
  is_prime = True
  for i in range(2,number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

my_value = int(input("Enter number to check if Prime / not Prime: "))
prime_checker(my_value)
