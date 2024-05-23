# # # # # # # import random

# # # # # # # randomGuess = random.randint(1, 101)
# # # # # # # attemptCounter = 0
# # # # # # # while True:
# # # # # # #     try:

# # # # # # #         userInput = int(input("Guess a number: "))

# # # # # # #         if userInput > randomGuess:
# # # # # # #             attemptCounter += 1
# # # # # # #             print("Too high, Try again!")

# # # # # # #         elif userInput < randomGuess:
# # # # # # #             attemptCounter += 1
# # # # # # #             print("Too low, Try again!")

# # # # # # #         else:
# # # # # # #             print(
# # # # # # #                 f"You've guessed it! you've attempted {attemptCounter} times!")
# # # # # # #             break

# # # # # # #     except ValueError:
# # # # # # #         print("Please type a number")


# # # # # # # for number in range(1, 101):
# # # # # # #     if number % 3 == 0 and number % 5 == 0:
# # # # # # #         print("FizzBuzz")

# # # # # # #     elif number % 3 == 0:
# # # # # # #         print("Fizz")

# # # # # # #     elif number % 5 == 0:
# # # # # # #         print("Buzz")
# # # # # # #     else:
# # # # # # #         print(number)


# # # # # # # userInput = int(input("Please enter a number: "))

# # # # # # # factors = [

# # # # # # # ]


# # # # # # # for i in range(1, userInput + 1):

# # # # # # #     if userInput % i == 0:
# # # # # # #         factors.append(i)

# # # # # # # print(f"The factors of {userInput} are {factors}")


# # # # # # count = 0
# # # # # # nameList = []

# # # # # # while count < 5:  # Changed to "<" to allow 5 names to be added.
# # # # # #     name = input("Please type a name to add to the list: ")
# # # # # #     nameList.append(name)
# # # # # #     count += 1

# # # # # # print(f"Here is your list:\n{nameList}")


# # # # # Exercise 8: Max of Three Numbers
# # # # # Write a function called max_of_three that takes three numbers as arguments and returns the maximum of the three numbers.

# def max_of_three(first_num, second_num, third_num):
#     if first_num > second_num and first_num > third_num:
#         return first_num
#     elif second_num > first_num and second_num > third_num:
#         return second_num
#     elif third_num > first_num and third_num > second_num:
#         return third_num
#     else:
#         return None


# print("Welcome to the Maximum Three Numbers! ")


# while True:
#     print()
#     firstNum = input("Please type your first number: ")
#     secondNum = input("Please type your second number: ")
#     thirdNum = input("Please type your third number: ")

#     # Check if all inputs can be converted to integers
#     if firstNum.isdigit() and secondNum.isdigit() and thirdNum.isdigit():
#         firstNum = int(firstNum)
#         secondNum = int(secondNum)
#         thirdNum = int(thirdNum)
#         result = max_of_three(firstNum, secondNum, thirdNum)
#         break
#     else:
#         print("Please type 3 integers")
#         continue

# print(f"{result} is the maximum number of {firstNum}, {secondNum}, and {thirdNum}")


# # # """
# # # Exercise 9: Calculate Power
# # # Write a function called calculate_power that takes two numbers as arguments: base and exponent.
# # # The function should calculate and return base raised to the power of exponent.
# # # You can use the ** operator for exponentiation.
# # # """


# # def calculate_power(base, exponent):
# #     result = base ** exponent
# #     return result


# # print("Welcome to calculate to the power!\n\nPlease provide two numbers so we can calculate!")
# # print("\n")

# # while True:
# #     baseNum = input("Please provide your base number: ")
# #     if baseNum.isdigit():
# #         baseNum = int(baseNum)
# #         break
# #     else:
# #         print("Please provide a base number.")
# #         continue

# # while True:
# #     exponentNum = input("Please provide your exponent: ")
# #     if exponentNum.isdigit():
# #         exponentNum = int(exponentNum)
# #         break
# #     else:
# #         print("Please provide an exponent number.")

# # expoCalc = calculate_power(baseNum, exponentNum)
# # print(f"{baseNum} to the power of {exponentNum} = {expoCalc}")

# # # import math


# # # def squareRoot(num):

# # #     result = math.sqrt(num)

# # #     return result


# # # while True:
# # #     userInput = int(input("Please type a number to find it's square root: "))

# # #     if userInput >= 0:
# # #         calcInput = squareRoot(userInput)
# # #         break

# # #     else:
# # #         print("Please type an integer ")
# # #         continue

# # # print(f"the square root of {userInput} is {int(calcInput)}")


# def pressureFinder(force, area):

#     pressure = force / area

#     return pressure


# print("Lets find the pressure using the formula P = F/A")
# while True:
#     forceInput = input("Please type your force number: ")
#     if forceInput.isdigit():
#         forceInput = int(forceInput)
#         break
#     else:
#         print("Please provide a force number DUDE")
#         continue

# while True:
#     areaInput = input("Please type your area number: ")
#     if areaInput.isdigit():
#         areaInput = int(areaInput)
#         break
#     else:
#         print('Please provide a area number DUDE')
#         continue

# result = pressureFinder(forceInput, areaInput)

# print(f"The Pressure of {forceInput} and {areaInput} is {result}")


def string_length(inputString):
    stringLength = len(inputString)

    return stringLength


userInput = (input("Please type the longest sentence you can think of: "))

result = string_length(userInput)

print(f"the length of that sentence is {result} characters.")
