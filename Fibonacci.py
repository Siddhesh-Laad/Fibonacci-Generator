import time

# Function to calculate Fibonacci number using iteration

def fibonacci_Iteration(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initializing variables for iterative approach
    
    prevNum = 0
    currentNum = 1

    # Iteratively compute Fibonacci numbers from 2 to n
     
    for i in range(2, n + 1):
        nextNum = prevNum + currentNum  # Calculate next Fibonacci number
        prevNum = currentNum # Update previous number
        currentNum = nextNum # Update current number

    return currentNum  # Return Fibonacci number for n

# Function to calculate Fibonacci number using recursion

def fibonacci_Recursion(n):
    if n == 0:
        return 0  # Base case: fib(0) = 0
    elif n == 1:
        return 1  # Base case: fib(1) = 1
    else:
        # Recursive calls to compute Fibonacci number for n

        return fibonacci_Recursion(n - 1) + fibonacci_Recursion(n - 2)

if __name__ == "__main__":
     # Prompt user for input

    num = int(input("Enter a number: "))

    # Calculate current time in seconds
    initial_time = time.time()

 # Calculate Fibonacci number using recursion
    print(f"Using recursion, fib({num}) = {fibonacci_Recursion(num)}")

    # Calculate Fibonacci number using iteration
    
    print(f"Using iteration, fib({num}) = {fibonacci_Iteration(num)}")
    print(f"It took {time.time() - initial_time} seconds")