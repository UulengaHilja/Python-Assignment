#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

radius_input = input("Enter the radius of the circle: ")
if radius_input.isnumeric():
    radius = int(radius_input)
    area = math.pi * radius ** 2
    print("Area of the circle is:", area)
    choice = input("Do you want to calculate the perimeter as well? (y/n): ")
    if choice == 'y':
        perimeter = 2 * math.pi * radius
        print("Perimeter of the circle is:", perimeter)
elif radius_input.replace('.', '').isdigit():
    radius = float(radius_input)
    area = math.pi * radius ** 2
    print("Area of the circle is:", area)
    choice = input("Do you want to calculate the perimeter as well? (y/n): ")
    if choice == 'y':
        perimeter = 2 * math.pi * radius
        print("Perimeter of the circle is:", perimeter)
else:
    print("Invalid input! Please enter a numeric value for the radius.")


# In[ ]:


# Check if there is a student named 'Maria' in students_profile dictionary
if 'Maria' in students_profile:
    # If exists remove 'ML' from her course
    students_profile['Maria'].remove('ML')
    print("Successfully removed 'ML' from Maria's course")
else:
    print("Maria is not in the students_profile dictionary")

# Take the input from the user as a substring
substring = input("Enter a substring: ")

# If that substring is present in string then display substring is present
if substring in string:
    print("Substring is present")
else:
    print("Substring is not present")


# In[ ]:


import numpy as np

# Define the two points
p1 = np.array([1, 2, 3])
p2 = np.array([4, 5, 6])

# Define the order
order = 2

# Calculate the distance
if order == 1:
    distance = np.sum(np.abs(p1 - p2))
    print("L1 norm distance:", distance)
elif order == 2:
    distance = np.sqrt(np.sum((p1 - p2) ** 2))
    print("L2 norm distance:", distance)
else:
    distance = np.power(np.sum(np.power(np.abs(p1 - p2), order)), 1/order)
    print(f"Minkowski distance (order {order}):", distance)


# In[ ]:


#Loops
#for loop
# take input from user for which number to print multiplication table
number = int(input("Enter a number: "))

# print multiplication table using for loop
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    
#While loop 
# take input from user for which number to print multiplication table
number = int(input("Enter a number: "))

# initialize counter variable
i = 1

# print multiplication table using while loop
print(f"Multiplication table of {number}:")
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1


# In[ ]:


#DNA Tempelate
# Define the template string
dna_template = 'AATCCGAAAATTCGGGAATTTTCGCGT'

# Define the mapper
mapper = {"T": "A", "A": "T", "G": "C", "C": "G"}

# Generate the complementary DNA template
dna_complementary = ""
for base in dna_template:
    dna_complementary += mapper[base]

# Print the results
print("DNA template:", dna_template)
print("Complementary DNA template:", dna_complementary)


# In[ ]:


import math

# Generate the Fibonacci series
f_series = [0, 1]
for i in range(2, 13):
    f_series.append(f_series[i-1] + f_series[i-2])

# Print the Fibonacci series
print("Fibonacci series:", f_series)

# Generate a list of n prime numbers
n = 10
prime_numbers = []
i = 2
while len(prime_numbers) < n:
    is_prime = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
    i += 1

# Print the list of prime numbers
print("List of prime numbers:", prime_numbers)

# Perform minmax normalization to the range [0,1] for data1
data1 = [1, 17, 12, 15, 30, 60, 48, 51, 89, 92, 54, 8]
X_min = min(data1)
X_max = max(data1)
data1_normalized = [(x - X_min) / (X_max - X_min) for x in data1]

# Print the normalized data1
print("Normalized data1 (minmax normalization to the range [0,1]):", data1_normalized)

# Perform minmax normalization to the range [-1,1] for data2
data2 = [-13, 2, -1, 7, 22, -32, 5, 15, -9, 13, 3, -2]
X_min = min(data2)
X_max = max(data2)
data2_normalized = [2 * (x - X_min) / (X_max - X_min) - 1 for x in data2]

# Print the normalized data2
print("Normalized data2 (minmax normalization to the range [-1,1]):", data2_normalized)


# In[ ]:


# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#Comparison of time complexity of these sorting algorithms:

Bubble Sort: O(n^2)
Selection Sort: O(n^2)
Insertion Sort: O(n^2)


# In[ ]:


def factorial(n):
    """
    This function calculates the factorial of a number.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the given number.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# In[ ]:


import math

def activation_function(func_name, x):
    """
    Takes an activation function name and a value and returns the output of the specified activation function.

    Parameters:
    func_name (str): The name of the activation function to use. Options are 'sigmoid', 'binary_step', 'relu', 'leaky_relu', and 'tanh'.
    x (float): The input value to the activation function.

    Returns:
    float: The output value of the specified activation function for the given input value.
    """
    if func_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif func_name == 'binary_step':
        return 1 if x >= 0 else 0
    elif func_name == 'relu':
        return max(0, x)
    elif func_name == 'leaky_relu':
        return max(0.1 * x, x)
    elif func_name == 'tanh':
        return math.tanh(x)
    else:
        raise ValueError(f"Activation function '{func_name}' is not supported.")

     print(activation_function('sigmoid', 0))    # Output: 0.5
   


# In[ ]:


def permutation(n, r):
    """
    Returns the number of permutations for 'r' objects from a set of 'n' objects where order matters.
    Formula: P(n, r) = n! / (n - r)!

    Parameters:
    n (int): Number of objects in the set
    r (int): Number of objects to be arranged

    Returns:
    int: Number of permutations for 'r' objects from a set of 'n' objects
    """
    return factorial(n) // factorial(n-r)

# Example to find the number of permutations of 4 objects from a set of 7 objects
p = permutation(7, 4)
print(p) # Output: 840


# In[ ]:


def perm_comb(kind='both', n=10, r=5):
    """
    Returns the permutation or combination, or both, of 'r' objects chosen from a set of 'n' objects where order matters
    and the formula is P(n, r) = n! / (n - r)! for permutation and C(n, r) = n! / (r! * (n - r)!) for combination.

    Parameters:
    kind (str): Determines what to return, either 'perm', 'comb', or 'both'. Default is 'both'.
    n (int): The number of objects to choose from. Default is 10.
    r (int): The number of objects to choose. Default is 5.

    Returns:
    If kind is 'perm', returns the permutation of 'r' objects chosen from 'n' objects.
    If kind is 'comb', returns the combination of 'r' objects chosen from 'n' objects.
    If kind is 'both', returns a tuple containing both the permutation and combination.
    """
    # Calculate permutation and combination
    perm = factorial(n) / factorial(n-r)
    comb = factorial(n) / (factorial(r) * factorial(n-r))

    # Determine what to return
    if kind == 'perm':
        return perm
    elif kind == 'comb':
        return comb
    else:
        return (perm, comb)

    >>> perm_comb('perm', 6, 3)
120.0
>>> perm_comb('comb', 6, 3)
20.0
>>> perm_comb('both', 6, 3)
(120.0, 20.0)
>>> perm_comb(n=4)
(24.0, 10.0)

    


# In[ ]:


# Function that takes any number of positional and keyword arguments:

def my_function(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
        
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}={value}")
        
#Example        
my_function("hello", 42, [1, 2, 3], name="John", age=30, city="New York")

