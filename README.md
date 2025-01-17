# Equation Quiz
## Overview
Welcome to the **Equation Quiz** manual where it is designed to help the user understand how to use the program, Equation Quiz and does not require any programming experience. 

## User Manual
The purpose of this quiz-like program is to generate simple random mathematical equations for the user to solve and essentially test one's knowledge. These equations can come in any of the following formats whereby the symbol "?" is what the user is trying to solve as shown below;

- 3 + ? = 12
- ? - 3 = 12
- 3 * 4 = ?
  
The equation will consist of two randomly generated factors i.e. the operands (two numbers) and the operator. Operators can be either; Addition, Subtraction, Multiplication or Division. 

### Main Features
1. User choice for number of equations
It will prompt the user how many equations they would like to solve and than ask them that many times except if its over the limit
2. Score Checker and Tracker
Users' answer's are validated to see if they're correct or not as well as tracked which the user can their total score at the very end of the quiz. 
3. Timed Answer
The program can measure how long it takes for the user to complete the quiz, adding that element of challenge whilst improving mental math skills.
4. User Streak
This unique feature is designed to display the current streak of the user.

#### Requirements
- A computer or laptop
- Python version 3.6 or higher installed on your computer
- Access to a terminal or command prompt


#### How to Run Program
1. Python version 3.7 or later installed locally

2. Download the python file from the repository accessed here: https://github.com/sameerahmahmood/if1-sum1-task1/blob/main/random_equation_generator.py

![screenshot_of_github_link](https://github.com/user-attachments/assets/3bb72379-6912-4199-8031-e525cb8f2f2b)

3. Store the file within a folder of your choice

![screenshot_of_chosen_folder](https://github.com/user-attachments/assets/177e1822-90ca-4124-a3a6-52490be3dba9
)
 
8. Using the search bar in the taskbar, navigate to the terminal or Command Prompt

9. Use the 'cd' command to direct into the folder where you saved the file

![example_of_cd_command](https://github.com/user-attachments/assets/90833d04-efc4-4aee-85a0-1ddfc4e9fa50)

10. Run the program using the command: ```python random_equation_generator.py```. 

![Example of command to run python file](https://github.com/user-attachments/assets/760af610-68a0-4e4e-835e-bfeb7279bc2b)


#### How to Use Program 
1. Run the game in the terminal using the following command
```python equation_quiz_generator.py```
2. Input how many equations you would like to solve e.g. the number "10"
3. Answer each equation as requested 
4. See output 

###### Example Gameplay
[example gif of the running program](![ezgif com-split](https://github.com/user-attachments/assets/1a8f8671-426f-4220-8616-c1fec545f466))

## Technical Documentation
### Overview
This part of the guide defines the technicalities of the program, Equation Quiz including the design, coding standards and being able to clone a repository from GitHub. 

### Cloning a Repository
Prior to running the program, it is important to know how to create a copy of the repository that stores the program file on one's computer.

1. Get the Repository URL
   
The repository page of this specific program is located on GitHub. Simply locate the repository and copy the URL from the search bar.

2. Terminal

Then search for a terminal for example Command Prompt.

4. Directory Navigation

Use the 'cd' command to navigate to a folder where you would like to clone the repository, as shown below. 

```cd <desired_folder>```

5. Git clone
Use the following command to clone the repository. 

```git clone <repository_url>```

6. Cloned Repository Navigation

In order to change the current directory into the cloned repository one, simply use the 'cd' command again but with cloned repository name instead like this:

```cd name_of_repository```

### Coding Standards
The next part of this document outlines coding standards which are a set of guidelines one follows to ensure the highest quality code and consistency.

#### Naming Conventions
For both variable and function names, snake_case following PEP8 standards was the main naming convention I used for example the variable that stores how many equations to solve "total_eqs". Furthermore,  I tried to make the names descriptive and include verb phrases. Examples include:

- user_score
- user_answer
- missing_var
- operand1
- operand2
- result
- true_answer

Function name examples:

- generate_components
- construct_equation
- format_equation
- check_user_score

#### Program Flow

Next I will discuss the structure of the program i.e. how each step is executed which will be sectioned into stages.

1. Program start-up
   
In the main function, it will prompt the user to input how many equations they would like to solve. Whilst doing so, it will validate their response ensuring that there inputs are correct. Otherwise the user is simply re-prompted. After that is a for loop that will loop through the total number of equations, requesting the user to solve the missing number each time. Each of the functions are also called and then it would output the outcome accordingly.

Inputs:
- total_eqs 
- user_answer
  
Outputs:
- user_score
- user_streak
- start_time
  
2. Generating the equation
  
The next stage includes the 'generate_function' function which randomly generating each of the components (operand1,operand2 and operator) from importing random. If division is to be selected, operand2 is to be a factor of the operand1 resulting in whole numbers for the sake of simplicity.

3. Constructing the equation
   
Afterwards, the 'construct_function' function will consutrct a simple equation as well as calculating the result of the equation i.e. the output of the operation. The program would then return calling the function 'format_equation' whilst still inside the 'construct_equation' function in order to improve modularity.

Inputs:
- operand1
- operand2
  
Outputs:
- formatted equation with one missing part(missing_var)
  
5. Formatting the equation
  
Subsequently, the equation would be formatted by the 'format_equation' function as mentioned above. It handles how the equation is going to look like for the user. It does this by randomly choosing one part of the equation - operand1, operand2 or result and assigning to the 'missing_var' variable which will be what the user will ultimately solve. It also will calculates the correct answer to the equation. 

Inputs:
- operand1
- operand2
- operator
- result
- equation
  
Outputs:
- equation
- true answer
6. Check the user score and streak

Inputs:
- user_answer
- true_answer
- user_score
- user_streak

Outputs:
- user_score
- user_streak
  
#### New and Existing Features 
Existing features:

- Ask user how many equations to solve
- Score validation
- Score tracking
- Basic error handling

New features:

- Number of equation limit: I had to do this underneath 'total_eqs' by setting a limit to the number of equations by assigning a variable called "maximum_eqs". 
- User streak: I made this by incorporating it into the check_user_score function by using an addition operation operator below user_score.
- Timed user session: I updated this by simply importing time into the file and then initialising it just as the quiz starts.
 
#### Testing 
For testing I implemented pytest unit tests for the tech_user_score function in a seperate file called test_equation_quiz_generator.py. 

#### Considerations
The structure and overall design of the program were done in a way that were:
1. Simple and easy to use
2. Modular
3. Readable 

#### Future Enhancements
- User choice in specific operation type or all 
- Highest streak tracker/ leaderboard: To be able to check your highest streak out of all of the users session 
- GUI: A Graphical User Interface for easier navigation and potential application development
