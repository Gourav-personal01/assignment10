import threading

def print_squares(numbers):
    for number in numbers:
        square = number ** 2
        print(f"Square of {number}: {square}")

def print_cubes(numbers):
    for number in numbers:
        cube = number ** 3
        print(f"Cube of {number}: {cube}")

# Create the list of numbers
numbers = [1, 2, 3, 4, 5]

# Create two threads, one for squares and one for cubes
thread_squares = threading.Thread(target=print_squares, args=(numbers,))
thread_cubes = threading.Thread(target=print_cubes, args=(numbers,))

# Start both threads
thread_squares.start()
thread_cubes.start()

# Wait for both threads to finish
thread_squares.join()
thread_cubes.join()
