import random

def Function_A(min, max):
    #Random Integer returned from this function.
    return random.randint(min, max) 

def Function_B():
    #Random operation symbol returned from this function.
    return random.choice(['+', '-', '*'])

def Function_C(num1, num2, operation):
    #Problem is defined as F-string
    Problem = f"{num1} {operation} {num2}"

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    return Problem, result

def Math_Quiz():
    Score = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        num1 = Function_A(1, 10)
        num2 = Function_A(1, 5)
        operation = Function_B()

        Problem, Answer = Function_C(num1, num2, operation)
        print(f"\nQuestion: {Problem}")
        
        try:
            #Get user input
            user_input = int(input("Enter your answer: "))

        except ValueError:
            # Handle the error if the user enters something that's not a valid integer
            print("Invalid input. Please enter a valid number.")

        except Exception as e:
            # Handle other unexpected errors
            print(f"An unexpected error occurred: {e}")

        if user_input == Answer:
            print("Correct! You earned a point.")
            Score += 1
        else:
            print(f"Wrong answer. The correct answer is {Answer}.")

    print(f"\nGame over! Your score is: {Score}/{t_q}")

if __name__ == "__main__":
    Math_Quiz()