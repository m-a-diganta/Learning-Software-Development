# Python is dynamically typed, meaning you don't need to declare variable types.
# Case sensitive 
# Python Data Types: numeric, string, boolean, set, sequence, mapping, None 
# Numeric types: int, float, complex (e.g. 3 + 4j)
# Mutable Data Types: list, set, dictionary 
# Immutable Data Types: integer, float, string, tuple, frozenset [if any change => a new object is created, new memory location is allocated]
# Memory location can be checked using the id() function
"""Data Type conversion: 
1. Explicit conversion using functions like int(), float(), str(), list(), tuple(), set(), dict() 
2. Implicit conversion (e.g. x= 5, y = 2.5, z = x + y => z is implicitly converted to float)"""

print("\n######################################################################################################################\n")

import math
# Example of arithmetic operations
x = 10
print("Square root of x:", math.sqrt(x))  
print("x raised to the power of 2:", math.pow(x, 2)) 
print("Ceiling of 2.3:", math.ceil(2.3))  
print("Floor of 2.7:", math.floor(2.7))  
print("Factorial of 5:", math.factorial(5))  
print("Sine of 30 degrees:", math.sin(math.radians(30)))  # trigonometric functions
print("Logarithm base 10 of 100:", math.log10(100))  # logarithmic functions
print("Absolute value of -5:", math.fabs(-5.22))  # absolute value, for integer value use abs()
print("Least common multiple of 10 and 2:", math.lcm(10, 2))  # least common multiple
print("Greatest common divisor of 10 and 2:", math.gcd(10, 2))  # greatest common divisor

# Operator precedence: ()   >   **   >   *, /, //, %   >   +, -

print("\n######################################################################################################################\n")

#For strings, use single, double or triple quotes for multi-line strings.
# String allows indexing and slicing 
# Common string methods: lower(), upper(), strip(), split(), join(), replace(), find(), count(), format(), startwith(), endswith(), capitalize(), swapcase(), isalnum(), isalpha(), isdigit(), isspace(), istitle()  
# Example of string manipulation
name = "  Alfessani Diganta "
print(name.lower()) 
print(name.upper()) 
print(name.strip())  # removes leading/trailing whitespace
print(name.split())  # splits by whitespace
print(name.replace("Alfessani", "Diganta"))  # replaces substring
print(joined_name := " ".join(name.split()))  # joins list into a string
print(name[0:5])  # Output:  Alfes (slicing from index 0 to 4)
# Use cases for string methods: Data cleaning, formatting, manipulation, Extracting substrings, Validation
print(name.find("Diganta"))  
print(name.count("a")) 

# Example of string concatenation
greeting = "Hello"
name = "Diganta"
print(greeting + " " + name ) 
print(f"{greeting} {name}")  # Using f-string for formatting
print("Hello {} {}".format(greeting, name))  # Using format() method
print("Hello %s %s" % (greeting, name))  # Using % formatting
# Use cases for strong formatting and concatenation: Building dynamic messages, URL construction, File paths, Data presentation

print("\n######################################################################################################################\n")

# If-Else Example:

x = 5
y = 10
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

print("\n######################################################################################################################\n")

# For loops and While loops Example:
for i in range(5):  
    print(f"Iteration {i}")
i = 0
while i < 5:  
    print(f"While loop iteration {i}")
    i += 1       


print("\n######################################################################################################################\n")

# Sequence Data Types:
# List: ordered, mutable, allows duplicates
# Tuple: ordered, immutable, allows duplicates
# Dictionary: unordered, mutable, key-value pairs
# Set: unordered, mutable, no duplicates, automatically removes duplicates
# Frozenset: unordered, immutable, no duplicates

print("\n######################################################################################################################\n")

# List Methods: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse()
my_list = [2, 8, 30, 30, 30, 5, 25]
my_list.append("appended value")  
print("List after append:", my_list)
my_list.extend([7, 8])  
print("List after extend:", my_list)
my_list.insert(2, "inserted value")  
print("List after insert:", my_list)
my_list.remove(30)  # removes the first occurrence of 30
print("List after remove:", my_list)
my_list.pop()  # removes the last element
print("List after pop:", my_list)
my_list.pop(-2)  # removes the element at index -2
print("List after pop(-2):", my_list)
my_list.index(8)  # returns the index of the first occurrence of 8
print("Index of 8:", my_list.index(8))
my_list.count(30)  # how many times 30 appears 
print("Count of 30:", my_list.count(30))
my_list2 = []
for i in my_list:  
    if isinstance(i, int):
        my_list2.append(i)
print("Filtered list with only integers:", my_list2)
my_list2.sort()  # in ascending order, must be homogeneous
print("List after sort:", my_list2) 
my_list2.reverse()
print("List after reverse:", my_list2)

print("\n######################################################################################################################\n")

# Tuple Methods: count(), index()
my_tuple = (1, 2, 3, 4, 5, 1, 2, 3)
print("Tuple:", my_tuple)
print("Count of 1 in tuple:", my_tuple.count(1)) 
print("Index of 2 in tuple:", my_tuple.index(2))  # returns the index of the first occurrence
print(list(my_tuple))  # converting tuple to list

print("\n######################################################################################################################\n") 

# Set Methods: add(), update(), remove(), discard(), pop(), clear(), union(), intersection(), difference()
my_set = {0, 2, 3, 4, 5}
my_set.add("added value")  
print("Set after add:", my_set)
my_set.update([7, 8])  # adds multiple elements
print("Set after update:", my_set)
my_set.remove(3)  # removes an element, raises KeyError if not found
print("Set after remove:", my_set)
my_set.discard(4)  # removes an element, does not raise error if not found
print("Set after discard:", my_set)
popped_value =my_set.pop()  # removes and returns an arbitrary element
print("Set after pop:", my_set, " and Popped value:", popped_value)
union = my_set.union({9, 10})  # returns a new set with elements from both sets
print("Union with {9, 10}:", union)
intersection = my_set.intersection({1, 2, 6})  # returns a new set with common elements
print("Intersection with {1, 2, 6}:", intersection)
difference = my_set.difference({1, 2})  # returns a new set with elements in my_set but not in the other set
print("Difference with {1, 2}:", difference)
print(my_set)
my_set.clear()  # removes all elements
print("Set after clear:", my_set)

print(" Is {1, 2} a subset of {0, 1, 2, 3, 4, 5}?", {1, 2}.issubset({0, 1, 2, 3, 4, 5}))
print(" Is {0, 1, 2, 3, 4, 5} a superset of {1, 2}?", {0, 1, 2, 3, 4, 5}.issuperset({1, 2}))

print("\n######################################################################################################################\n") 

# Dictionary Methods: keys(), values(), items(), get(), pop(), popitem(), update(), clear()
my_dict = {'name': 'Alfessani', 'age': 25, 'city': 'Dhaka'}
print("Dictionary:", my_dict)
print("Keys:", my_dict.keys())  
print("Values:", my_dict.values())  
print("Items:", my_dict.items())  
print("Get value for 'name':", my_dict.get('name'))  
my_dict['country'] = 'Bangladesh'  
print("Dictionary after adding 'country':", my_dict)
my_dict.pop('age')  # removes the specified key and returns its value
print("Dictionary after pop('age'):", my_dict)
popped_item = my_dict.popitem()  # removes and returns the last inserted key-value pair
print("Dictionary after popitem():", my_dict, " and Popped item:", popped_item)
my_dict.update({'profession': 'Engineer'})  # updates the dictionary with new key-value pairs
print("Dictionary after update:", my_dict)
my_dict.clear()  
print("Dictionary after clear:", my_dict)   

print("\n######################################################################################################################\n")

# To avoid errors, use try-except blocks for exception handling
# Example:
try:
    num = int("one")
except Exception as e:
    print(f"Error: {e}")

print("\n######################################################################################################################\n") 

# Functions: to encapsulate reusable code, to improve readability, and to avoid repetition
def greatest_number(a, b, c): # a, b, c are parameters
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Greatest number among 5, 10, 15 is:", greatest_number(5, 10, 15)) # 5, 10, 15 are arguments 
print("Greatest number among 20, 10, 15 is:", greatest_number(20, 10, 15))

# If number of arguments is variable, use *args, Variable length arguments
def sum_of_numbers(*args):
    return sum(args)
print("Sum of 1, 2, 3, 4, 5 is:", sum_of_numbers(1, 2, 3, 4, 5))

# Keyword arguments: to pass arguments by name, *kwargs
def print_info(name, age, **kwargs):
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info("Alfessani", 25, city="Dhaka", profession="Engineer")

# Lambda functions: for small, anonymous functions
add = lambda x, y: x + y
print("Sum of 5 and 10 using lambda function:", add(5, 10))

# Local variables are defined within a function and cannot be accessed outside. [Can make it global using the global keyword]
# Global variables are defined outside any function and can be accessed anywhere.

print("\n######################################################################################################################\n") 

# File/ Directory Handling
# Modes: 'r' (read), 'w' (write), 'a' (append), 'r+' (read and write), 'b' (binary mode)

# with statement ensures the file is properly closed after writing
with open('example.txt', 'w') as file:  # 'w' mode creates a new file or overwrites an existing one replacing its content.
    print("created")
    file.write("Replace the line!\n")

with open('example.txt', 'r') as file: 
    content = file.read()  
    print("File content:", content)

import os
os.rename('example.txt', 'new_example.txt')  
# os.remove('new_example.txt') 

with open('new_example.txt', 'a') as file:  # keeps the previous content
    file.write("This is an appended line.\n")

with open('new_example.txt', 'rb') as file:
    content = file.read()  # reading in binary mode
    print("Binary file content:", content)

# Directory operations
if not os.path.exists('new_directory'):
    os.makedirs('new_directory')  
    print("Directory created.")

files = os.listdir('new_directory')
print("Files in 'new_directory':", files)
files2 = os.listdir('.')
print("Files in current directory:", files2)
# os.rename('new_directory', 'new_directory2') 
# os.rmdir('new_directory2') # remove the files first, then the directory
# os.chdir('new_directory')  # change current working directory to 'new_directory'

print("\n######################################################################################################################\n") 

# Working with Zip Files
import zipfile
with zipfile.ZipFile('zip_example.zip', 'w') as zipf:
    zipf.write('new_example.txt', arcname='new_example_zip.txt')  # arcname is the name in the zip file     
print("Zipped files:", zipf.namelist()) 
with zipfile.ZipFile('zip_example.zip', 'r') as zipf:
    zipf.extractall('extracted_files')  # extracts to 'extracted_files' directory 
    zipf.extract('new_example_zip.txt', 'extracted_files')  # extracts a specific file

# Check if a file exists
if os.path.exists('new_example.txt'): 
    print("'new_example.txt' exists.")
else:
    print("'new_example.txt' does not exist.")

import shutil
# Copying files
shutil.copy('new_example.txt', 'new_directory/new_example_copy.txt')  
# Moving files
shutil.move('new_example.txt', 'new_directory/new_example_moved.txt')  
shutil.make_archive('archive_example', 'zip', 'new_directory')  # new_zip_name, format, root_dir

print("\n######################################################################################################################\n") 

# CSV File Handling
import csv

"""
data = [
    ['Name', 'Age', 'City', 'Country', 'Profession'],
    ['Alfessani', 25, 'Dhaka', 'Bangladesh', 'Engineer'],
    ['Diganta', 30, 'Chittagong', 'Bangladesh', 'Doctor'],
    ['John', 28, 'New York', 'USA', 'Teacher'], 
    ['Jane', 22, 'London', 'UK', 'Designer'],
    ['Alice', 27, 'Sydney', 'Australia', 'Scientist'],
]
os.mkdir('csv_folder') if not os.path.exists('csv_folder') else None
with open ('csv_folder/csv_data.csv', 'w') as file:
    csv_file = csv.writer(file)
    csv_file.writerows(data)  # write multiple rows at once
    print("CSV file created with data.") 
"""

with open('csv_folder/csv_data.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)  

print("\n######################################################################################################################\n")

# Multiple Exceptions Handling [try-except blocks to avoid program crashes]
try:
    with open('new_directory/test1.text', 'r') as file:
        content = file.read()
        result = 10 / 0  
        print(result)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except ZeroDivisionError as e:
    print(f"Division by zero error: {e}")
except ValueError as e:
    print(f"Value error: {e}")      
except TypeError as e:
    print(f"Type error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed, whether an error occurred or not.")

print("\n######################################################################################################################\n")

# Working with JSON Files

# JSON (JavaScript Object Notation) => lightweight data interchange format => easy to read and write for humans and machines => Language Independent
# Used for => Data exchange between web applications and servers => Frontend to Backend Data Transfer or Backend to Backend Data Transfer 
# JSON do not support comments, \b, \f, \n, \r, \t, \v 

# Key functions: 
# json.dump() to write JSON data to a file [works with file objects]
# json.load() to read JSON data from a file [works with file objects]
# json.dumps() to convert Python objects to JSON strings [works with strings]
# json.loads() to parse JSON strings into Python objects [works with strings]

import json
data = {
    "name": "Alfessani",
    "age": 25,
    "city": "Dhaka",
    "country": "Bangladesh",
    "skills": ["Python", "JavaScript", "HTML", "CSS"],
    "is_student": True,
    "education": {
        "degree": "Bachelor's",
        "field": "Computer Science",
        "university": "University of Dhaka"
    }
}

# Python Object => JSON String
json_string = json.dumps(data, indent=4) 
print("JSON String:\n", json_string)

# JSON String => Python Object
parsed_object = json.loads(json_string)
print("\nParsed JSON Data:\n", parsed_object)
print("Name:", parsed_object['name'])

# Writing JSON data to a file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  

# Reading JSON data from a file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print("\nLoaded JSON Data from file:\n", loaded_data)
    print("Name from loaded data:", loaded_data['name'])

print("\n######################################################################################################################\n")

# Working with Datetime
from datetime import datetime, timedelta
# Current date and time
curr_dateTime = datetime.now()
print(curr_dateTime)
print("Current Date:", curr_dateTime.date())
print("Current Time:", curr_dateTime.time())
print("Current Year:", curr_dateTime.year)
print("Current Month:", curr_dateTime.month)
print("Current Day:", curr_dateTime.day)
print("Current Hour:", curr_dateTime.hour)
print("Current Minute:", curr_dateTime.minute)
print("Current Second:", curr_dateTime.second)
print("Current Microsecond:", curr_dateTime.microsecond)
# Formatting date and time
formatted_date = curr_dateTime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_date)
# Parsing date and time from a string
date_string = "2023-10-01 12:30:45"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date and Time:", parsed_date)

# Date arithmetic
date1 = datetime(2023, 10, 1)
date2 = datetime(2023, 10, 15)
delta = date2 - date1
print("Difference between date1 and date2:", delta.days, "days")

new_date = date1 + timedelta(days=5, hours=3, minutes=30)
print("New Date after adding timedelta:", new_date)

print("\n######################################################################################################################\n")

# Working with Modules

# from Calculator_Module import add, subtract, divide (adds only specific functions)
import Calculator_Module as calc
print("Addition of 5 and 10 using Calculator_Module:", calc.add(5, 10))
print("Subtraction of 10 and 5 using Calculator_Module:", calc.subtract(10, 5))

# Built-in Modules: math, os, sys, datetime, json, csv, random, re, collections, itertools
import os
print("Current Working Directory:", os.getcwd())  
print("List of files in current directory:", os.listdir('.'))  

import sys
print("Python Version:", sys.version)  
print("Python Executable Path:", sys.executable)  

print("\n\n")
import http.client
conn = http.client.HTTPSConnection("dummyjson.com")
conn.request("GET", "/products")
response = conn.getresponse()
print("Response Status:", response.status)
print("Response Reason:", response.reason)
# read only 20 data 
data = response.read(500)
print("Response Data:", data.decode('utf-8'))  # decode bytes to string
conn.close()
conn.request("GET", "/todos")
response = conn.getresponse()
print("Response Status:", response.status)
print(response.read())
conn.close()

print("\n\n")
import subprocess
# Running a shell command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
result2 = subprocess.run(['python3', '--version'], capture_output=True, text=True)
print("Command Output:\n", result.stdout)
if result.stderr:
    print("Command Error:\n", result.stderr)
print("Python Version Output:\n", result2.stdout)
if result2.stderr:
    print("Python Version Error:\n", result2.stderr)

print("\n")
import hashlib # for hashing 
# Hashing a string using SHA-256
hash_object = hashlib.sha256(b'RandomPass123') # b'' indicates a byte string
hex_dig = hash_object.hexdigest() # converts the hash to a hexadecimal string
print("SHA-256 Hash:", hex_dig)

print("\n######################################################################################################################\n")

# User defined Multi-file Module / Package Development
# Package Name = Folder Name = Namespace => a file named __init__.py is required as root file  => import all modules in the init.py file
# Package Structure:
# my_package/
# ├── __init__.py
# ├── Max_module.py
# ├── Min_module.py

import my_package 
print("Max of 5, 10, 15 using Max_module:", my_package.Max_module.max(5, 10, 15))
print("Min of 6, 4, 15 using Min_module:", my_package.Min_module.min(6, 4, 15))



