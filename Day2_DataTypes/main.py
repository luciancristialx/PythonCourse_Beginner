# Understanding Data Types

#String
#print("Hello"[0]) #subscripting - print 'H'

#print("Hello"[4]) #subscripting - print 'o'

#Integer
#print(123+345)

#Float (decimal points)

#Boolean (True / False)

#num_char = len(input("What is your name?\n"))
#print(type(num_char))
#print("Your name has "+str(num_char)+" characters")

#print(round(8/3))
#print(round(8/3,2))

#score=0
#height=1.8
#isWinning=True
#f-string
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

print("Welcome to the tip calculator.")
bill_value = float(input("What was the total bill? $"))
tip_value = int(input("What percentage would you like to give? 10,12 or 15? "))
split_to = int(input("How many people to split the bill? "))
total_bill = bill_value + (tip_value/100 * bill_value)
value_per_person = total_bill /split_to
final_amount = round(value_per_person,2)
print(f"Each person should pay: ${final_amount}")


