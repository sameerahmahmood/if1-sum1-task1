#importing random for randomising operations including the operands, operator and equation order
import random 
#importing time for timing the user session
import time

print("Welcome to Equation Quiz!!")

def main():
    """ Random equation generator that generates simple equations using random numbers for users to solve as quickly as possible. 
        It is in a quiz format and has functionalities for generating, constructing and formatting equations. 
        It also keeps track of the users score and streak. 
    """

    while True:
        try:
            total_eqs = int(input("How many equations would you to like to solve?: "))
            maximum_eqs = 100
            if total_eqs > maximum_eqs:
                print("Number of equations exceeded. Please enter a number less than 100.")
            elif total_eqs <= 0:
                print("Number cannot be negative or 0. Please try again")
            else:
                #if user inputs valid number, break the loop
                break
        except ValueError :
            #if the user input invalid type, prompt the user again
            print("Invalid input. Please enter a number. ")

    #initialise the user score
    user_score = 0
    #initialise streak counter
    user_streak = 0 
    start_time = time.time()
    #loop through the total number of equations
    for _ in range(total_eqs):
        # for each equation, generate the random operands and operator
        num1, num2, operator = generate_components()
        # construct the equation and get correct ansewr using random components
        equation, true_answer = construct_equation(num1, num2, operator)
        #prints the equation to the user
        print(equation)
        while True:
            try:
                user_answer = float(input("Please solve the missing number: "))
                break
            except ValueError:
                print("Invalid Input. Please enter a number")
        #checking the user's answer and updating their score aswell as streak
        user_score, user_streak = check_user_score(user_answer, true_answer, user_score, user_streak)
        print(f"Current Streak: {user_streak}")
    

    end_time = time.time()
    #calculates the time taken by the user and rounds it
    user_time = round(end_time - start_time)   
    print(f"Your final score is: {user_score} out of {total_eqs}") 
    print(f"Time taken: {user_time} seconds!")

def generate_components():
    """
    Generates random operands and operator for the equation.
    For division, the second operand is a multiple of the first operand.
    """

    operators = ["+", "x", "-", "/"]
    #gets a random operator from the list of operators
    operator = random.choice(operators)
    #if division, results in operand2 being a factor of operand1 
    if operator == "/":
        operand2 = random.randint(1,10)
        operand1 = operand2 * random.randint(1,10)
    else:
        operand1 = random.randint(1,10)
        operand2 = random.randint(1,10)
    #returns random operands and operator for equation construction 
    return operand1,operand2, operator

def construct_equation(operand1, operand2, operator):
    """
    Constructs the equation based on the randomly generated components including operands and operator.
    Calculates the result of the equation.
    """
    #checks the operator and performs the operation on operands
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "x":
        result = operand1 * operand2
    else:
        result = round(operand1 / operand2)

    #returns formated equation which is created below
    return format_equation(operand1, operand2, operator, result)

def format_equation(operand1, operand2, operator, result):
    """ Formats the equation by randomly selecting a missing part of the equation for the user to solve. """

    #randomly selects the missing part of the equation
    missing_var = random.choice([operand1, operand2, result])
    #reorders the equation based on the missing part for complexity
    if missing_var == operand1:
        equation = f"? {operator} {operand2} = {result}"
        true_answer = operand1
    elif missing_var == operand2:
        equation = f"{operand1} {operator} ? =  {result}"
        true_answer = operand2
    else:
        equation = f"{operand1} {operator} {operand2} = ?"
        true_answer = result
    #returns the formatted equation and true answer
    return equation, true_answer

def check_user_score(user_answer, true_answer, user_score, user_streak):
    """
    Checks the user's answer and updates their score incrementally.
    As well as updating the user's streak each time they get a correct answer.
    """
    #if user's answer is right, increment score and streak
    if user_answer == true_answer:
        print("Correct! Well done!")
        user_score += 1
        user_streak += 1
    #otherwise print correct answer and reset streak
    else:
        print(f"Wrong, the correct answer is {true_answer}")
        user_streak = 0
    #
    return user_score, user_streak


if __name__ == "__main__":
    main()
