# Equation Quiz
## Overview 
Welcome to the **Equation Quiz** manual where it is designed to help the user understand how to use the program, Equation Quiz and does not require any programming experience. 

## User Manual
The purpose of this quiz-like program is to generate simple random mathematical equations for the user to solve and essentially test one's knowledge. These equations can come in any of the following formats whereby the symbol "?" or question mark is what the user is trying to solve as shown below;

- 3 + ? = 12
- ? - 3 = 12
- 3 * 4 = ?
  
In the equation will consist of two randomly generated factors i.e. the operands (two numbers) and the operation. Operations can be either; Addition, Subtraction, Multiplication or Division. The third and final part of the equation is the missing part or 'question mark' which is the number the user will be solving as mentioned in the above. 

### Main Features
1. User choice for number of equations
One of the features of this program is that it will prompt the user how many equations they would like to solve and than ask them that many times.
2. Timed Answer
Equation Quiz is able to time the user's session measuring how long it takes for them to complete the quiz. The timer will start when the actual quiz part of the program starts (excluding any prior activities) and will stop as soon as the user completes the quiz. This feature overall adds that element of challenge and encourages users to play again whilst improving mental math skills.
4. User Streak
The user streak is another unique feature designed to display the current streak of the user i.e. how many questions in the quiz they have got correct. 
5. Score tracker
At the end of the quiz, the user is able to see how many equations they solved correctly out of how many they wanted to solve. 

#### Requirements
- A computer or laptop running any of these operating systems; Windows, macOS or Linux
- Python version 3.6 or higher installed on your computer
- Access to a terminal or command prompt


#### How to Run Program
1. Python version 3.7 or later installed locally
2. Download the python file from the repository accessed via this link: https://github.com/sameerahmahmood/if1-sum1-task1/blob/main/random_equation_generator.py

An example screenshot is shown below.
![Example Screenshot](https://github.com/user-attachments/assets/3bb72379-6912-4199-8031-e525cb8f2f2b)

3. Store the file within a folder of your choice

An example screenshot is shown below.
![Example Screenshot](https://github.com/user-attachments/assets/177e1822-90ca-4124-a3a6-52490be3dba9
)
 
8. Using the search bar in the taskbar, navigate to the terminal or Command Prompt
9. Use the 'cd' command to direct into the folder where you saved the file

An example screenshot is shown below.
![Example Screenshot](https://github.com/user-attachments/assets/90833d04-efc4-4aee-85a0-1ddfc4e9fa50)
10. Run the program using the command python <name_of_file.py>. In this case, it would be ```python random_equation_generator.py``` but the name will vary depending on what file you are trying to run. 
![Example of command to run python file](https://github.com/user-attachments/assets/760af610-68a0-4e4e-835e-bfeb7279bc2b)


#### How to Use Program 
1. Run the game in the terminal using the following command
```python equation_quiz_generator.py```
2. Input how many equations you would like to solve e.g. the number "10"
3. 

###### Example Gameplay
[example gif of the running program](![ezgif com-split](https://github.com/user-attachments/assets/1a8f8671-426f-4220-8616-c1fec545f466)
)
## Technical Documentation
### Overview
This part of the guide demonstrates the technical side of the program, Equation Quize including the Design, Coding Standards as well as being able to clone a reponsitory from collaboration platform such as GitHub. 

### Cloning a Repository
Prior to running the program, it is important to know how to create a copy of the repository that stores the program file on one's computer which allows for using, editing and updating changes back the repository in real time and version control. 

1. Get the Repository URL
   
The repository page of this specific program is located on the popular software developer collab platform called GitHub. Simply locate the repository of choice and copy the URL from the search bar.

2. Terminal

Then search for a terminal for example Command Prompt or Windows Powershell and Bash if you are working with Linux.

4. Directory Navigation

Use the 'cd' command navigate to a folder where you would like to clone the repository, as shown below. 

```cd <desired_folder>```

5. Using the git clone Command

```git clone <repository_url>```

6. Cloned Repository Navigation

In order to change the current directory into the cloned repository directory, simply use the 'cd' command again but with cloned repository name instead like this:

```cd name_of_repository```

From there, one is able to access and run the python file which includes the program itself. 

### Coding Standards
The next part of this document outlnies coding standards which are a set of practices and guidelines one follows to ensure the highest quality code and consistency. Below are some examples of general coding standards:
#### Naming Conventions
For this section, naming conventions will be dicussed specifically for things like variables and functions. For variables, snake_case is the main naming convention I used for example the variable that stores how many equations to solve "total_eqs". The word "total" is self-explanatory. Then I attached an underscore after it and a shortened word for equation called "eqs" to improve readability. This convention also applied to function names. I tried to implement descriptive names and verb phrases for my variables and function names. Some examples include:
- user_score
- user_answer
- missing_var
- operator
Function name examples:
- generate_components
- construct_equation
- format_equation
- check_user_score
#### Program Flow

Next I will discuss the structure of the program i.e. how each step is executed. The program flow is sectioned into phases:
1. Program startup
The program will firstly greet the user with a welcome message. In the main function, it will  prompt the user to input how many equations they would like to solve. Whilst doing so, it will validate their response ensuring that the input is positive, not over the equation limit and/or any other invalid inputs. If the input happens to invalid, the user is simply re-prompted. Other things like their score and streak as well as timer will be initialised.
Main function inputs:
- total_eqs 
- user_answer
Main function outputs:
- current streak of the user
- user's final score
- user's time taken during the quiz
- 
2. Generating the equation randomly 
The next stage includes a function called 'generate_function' randomly generating each of the components (operand1,operand2 and operator) from the random import statement. If division is to be selected, I decided that the second number to be generated i.e. operand2 be a factor of the first number (operand1) resulting in whole numbers for the sake of simplicity.

3. Constructing the equation
After generating the components, the next step is the creation of the equation, ensuring that it is valid using the 'construct_function'. At this point the program will use those randomly generated numbers from the prior function to construct a simple equation. It will also calculate the result of the equation i.e. the produced output. After this, instead of having lots of code in what function, I returned calling the function 'format_equation' whilst still inside the 'construct_equation' function in order to improve modularity.
Inputs:
- operand1
5. Formatting the equation
Subsequently, the equation needs to be formatted which done with the use of the 'format_equation' function as mentioned above. This stage is necessary as it handles how the equation is going to look like for the user. It does this by randomly hiding one part of the equation and assigning it as a 'missing_var' variable. This variable contains the value the user is going to attempt to solve.

6. Check the user score and streak

#### New and Existing Features 
Existing features 

New features 
1. 
#### Testing and Validation 

#### Considerations

1. Simple and easy to use
2. Modularity
3. Readability 

#### Future Enhancements
- User choice in the operation type for example: Addition, Multiplication, Division, Subtraction or all
- Highest streak tracker: In the future its possible to check your highest streak out of all of the users session 
- GUI: A Graphical User Interface for easier navigation and potential mobile application development
