import random 
""" Random equation generator that generates simple equations using random numbers"""

print("Welcome to the Random Equation generator!")

def main():
    while True:
        try:
            total_eqs = int(input("How many equations would you to like to solve?: "))
            #if user inputs valid number, break the loop
            break
        except ValueError:
            #if the user input invalid number, prompt the user again
            print("Invalid Input. Please enter a valid number")

    #initialise the user score
    user_score = 0
    #loop through the total number of equations
    for _ in range(total_eqs):
        # for each equation, generate the random operands and operator
        num1, num2, operator = generate_components()
        # construct the equation and get correct ansewr using random components
        equation, true_answer = construct_equation(num1, num2, operator)
        #prints the equation to the user
        print(equation)
        user_answer = float(input("Please input your answer: "))
        #checking the user's answer and updating their score
        user_score = check_user_score(user_answer, true_answer, user_score)
    # gives users their final score    
    print(f"Your final score is {user_score}/{total_eqs}")

def generate_components():
    """Generates random operands and operator for the equation."""

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
    return operand1,operand2, operator

def construct_equation(operand1, operand2, operator):
    """
    Constructs an equation with a missing variable for user to solve and the random components.
    Calculates the true answer of the equation.
    """
    #checks the operator and performs the operation on operands
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "x":
        result = operand1 * operand2
    else:
        result = round(operand1 / operand2, 1)
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

    return equation, true_answer


def check_user_score(user_answer, true_answer, user_score):
    """Checks the user's answer and updates their score incrementally"""

    if user_answer == true_answer:
        print("Correct! Well done!")
        user_score += 1
    else:
        print(f"Wrong, the correct answer is {true_answer}")
    return user_score


if __name__ == "__main__":
    main()