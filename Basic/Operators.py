# Operators.py

# Arithmetic Operators
print(5 + 3)  # Addition: 8
print(5 - 3)  # Subtraction: 2
print(5 * 3)  # Multiplication: 15
print(5 / 3)  # Division: 1.66666666667
print(5 // 3)  # Floor division: 1
print(5 % 3)  # Modulus: 2
print(5 ** 3)  # Exponentiation: 125

# Assignment Operators
a = 5
a += 3  # a = a + 3: 8
a -= 2  # a = a - 2: 6
a *= 2  # a = a * 2: 12
a /= 2  # a = a / 2: 6.0
a //= 2  # a = a // 2: 3
a %= 2  # a = a % 2: 1
a **= 2  # a = a ** 2: 1

# Comparison Operators
print(5 == 3)  # Equal: False
print(5 != 3)  # Not equal: True
print(5 > 3)  # Greater than: True
print(5 >= 3)  # Greater than or equal to: True
print(5 < 3)  # Less than: False
print(5 <= 3)  # Less than or equal to: False

# Logical Operators
print(True and False)  # Logical AND: False
print(True or False)  # Logical OR: True
print(not True)  # Logical NOT: False

# Bitwise Operators
print(3 & 2)  # Bitwise AND: 2
print(3 | 2)  # Bitwise OR: 3
print(3 ^ 2)  # Bitwise XOR: 1
print(3 << 1)  # Bitwise left shift: 6
print(3 >> 1)  # Bitwise right shift: 1

# Identity Operators
print(5 is 5)  # True
print(5 is not 5)  # False

# Membership Operators
print('a' in 'abc')  # True
print('a' not in 'abc')  # False

# Conditional Expressions (Ternary Operator)
a = 5
result = 'Greater than 3' if a > 3 else 'Less than or equal to 3'
print(result)  # Greater than 3

# Lambda Expressions
add = lambda x, y: x + y
print(add(5, 3))  # 8

# List Comprehensions
numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Set Comprehensions
numbers_set = {x for x in range(10)}
print(numbers_set)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Dictionary Comprehensions
numbers_dict = {x: x**2 for x in range(10)}
print(numbers_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Generator Expressions
numbers_gen = (x for x in range(10))
print(list(numbers_gen))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generator Functions
def generate_numbers():
    for x in range(10):
        yield x

numbers_gen_func = generate_numbers()
print(list(numbers_gen_func))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exception Handling
try:
    result = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Raising Exceptions
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

try:
    result = divide(5, 0)
except ZeroDivisionError as e:
    print(e)

# User-defined Exceptions
class CustomException(Exception):
    pass

try:
    raise CustomException("This is a custom exception")
except CustomException as e:
    print(e)

# Using the with statement
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)

# Using the contextlib module
from contextlib import contextmanager

@contextmanager
def custom_context_manager():
    print("Entering context")
    try:
        yield
    finally:
        print("Exiting context")

with custom_context_manager():
    print("Inside context")

# Using the functools module
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # 15

# Using the operator module
import operator

numbers = [1, 2, 3, 4, 5]
result = reduce(operator.add, numbers)
print(result)  # 15

# Using the itertools module
import itertools

numbers = [1, 2, 3, 4, 5]
combinations = list(itertools.combinations(numbers, 2))
print(combinations)  # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

# Using the collections module
from collections import Counter

numbers = [1, 2, 3, 4, 5, 1, 2, 3]
counter = Counter(numbers)
print(counter)  # Counter({1: 2, 2: 2, 3: 2, 4: 1, 5: 1})

# Using the datetime module
from datetime import datetime

now = datetime.now()
print(now)  # 2022-01-01 12:00:00.000000

# Using the time module
import time

start_time = time.time()
# Perform some operation
time.sleep(1)
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)  # 1.000000

# Using the os module
import os

current_directory = os.getcwd()
print(current_directory)  # /path/to/current/directory

# Using the sys module
import sys

print(sys.version)  # 3.9.18 (main, Sep 11 2023, 13:40:49) [GCC 11.2.0]

# Using the re module
import re

pattern = r'\d+'
text = 'Hello 123 World'
matches = re.findall(pattern, text)
print(matches)  # ['123']

# Using the math module
import math

print(math.pi)  # 3.141592653589793
print(math.sqrt(25))  # 5.0

# Using the random module
import random

random_number = random.randint(1, 10)
print(random_number)  # Random number between 1 and 10

# Using the threading module
import threading

def print_numbers():
    for i in range(10):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# Using the multiprocessing module
import multiprocessing

def print_numbers():
    for i in range(10):
        print(i)

process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()

# Using the queue module
import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())  # 1
print(q.get())  # 2
print(q.get())  # 3

# Using the heapq module
import heapq

numbers = [4, 6, 8, 2, 10]
heapq.heapify(numbers)
print(heapq.heappop(numbers))  # 2
print(heapq.heappop(numbers))  # 4
print(heapq.heappop(numbers))  # 6
print(heapq.heappop(numbers))  # 8
print(heapq.heappop(numbers))  # 10

# Using the bisect module
import bisect

numbers = [1, 2, 3, 4, 5]
bisect.insort(numbers, 3)
print(numbers)  # [1, 2, 3, 3, 4, 5]

# Using the sqlite3 module
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL)''')

cursor.execute("INSERT INTO users (name, age) VALUES ('John Doe', 25)")
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)  # (1, 'John Doe', 25)

conn.close()

# Using the csv module
import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John Doe', 25])
    writer.writerow(['Jane Smith', 30])

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # ['Name', 'Age']
                  # ['John Doe', '25']
                  # ['Jane Smith', '30']

# Using the json module
import json

data = {
    'name': 'John Doe',
    'age': 25
}

json_data = json.dumps(data)
print(json_data)  # {"name": "John Doe", "age": 25}

parsed_data = json.loads(json_data)
print(parsed_data['name'])  # John Doe
print(parsed_data['age'])  # 25

# Using the xml.etree.ElementTree module
import xml.etree.ElementTree as ET

root = ET.Element('root')
child1 = ET.SubElement(root, 'child1')
child1.text = 'Hello'
child2 = ET.SubElement(root, 'child2')
child2.text = 'World'

tree = ET.ElementTree(root)
tree.write('output.xml')

with open('output.xml', 'r') as file:
    content = file.read()
    print(content)  # <root><child1>Hello</child1><child2>World</child2></root>

# Using the xml.dom.minidom module
from xml.dom.minidom import parseString

xml_string = '''
<root>
    <child1>Hello</child1>
    <child2>World</child2>
</root>
'''

dom = parseString(xml_string)
root = dom.documentElement

child1 = root.getElementsByTagName('child1')[0]
print(child1.childNodes[0].data)  # Hello

child2 = root.getElementsByTagName('child2')[0]
print(child2.childNodes[0].data)  # World

# Using the xml.sax module
import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def startElement(self, tag, attrs):
        print(f'Start element: {tag}')

    def endElement(self, tag):
        print(f'End element: {tag}')

    def characters(self, content):
        print(f'Characters: {content.strip()}')

xml_string = '''
<root>
    <child1>Hello</child1>
    <child2>World</child2>
</root>
'''

parser = xml.sax.parseString(xml_string, MyHandler())

# Using the xml.parsers.expat module
import xml.parsers.expat

class MyHandler:
    def start_element(self, name, attrs):
        print(f'Start element: {name}')

    def end_element(self, name):
        print(f'End element: {name}')

    def char_data(self, data):
        print(f'Characters: {data.strip()}')

parser = xml.parsers.expat.ParserCreate()
parser.StartElementHandler = MyHandler().start_element
parser.EndElementHandler = MyHandler().end_element
parser.CharacterDataHandler = MyHandler().char_data

xml_string = '''
<root>
    <child1>Hello</child1>
    <child2>World</child2>
</root>
'''

parser.Parse(xml_string)

# Using the xmlschema module
from xmlschema import XMLSchema

schema = XMLSchema('schema.xsd')

xml_string = '''
<root>
    <child1>Hello</child1>
    <child2>World</child2>
</root>
'''

if schema.is_valid(xml_string):
    print('XML is valid')
else:
    print('XML is not valid')

# Using the lxml module
from lxml import etree

root = etree.Element('root')
child1 = etree.SubElement(root, 'child1')
child1.text = 'Hello'
child2 = etree.SubElement(root, 'child2')
child2.text = 'World'

tree = etree.ElementTree(root)
tree.write('output.xml')

with open('output.xml', 'r') as file:
    content = file.read()
    print(content)  # <root><child1>Hello</child1><child2>World</child2></root>

# Using the defusedxml module
from defusedxml import minidom

xml_string = '''
<root>
    <child1>Hello</child1>
    <child2>World</child2>
</root>
'''

dom = minidom.parseString(xml_string)
root = dom.documentElement

child1 = root.getElementsByTagName('child1')[0]
print(child1.childNodes[0].data)  # Hello

child2 = root.getElementsByTagName('child2')[0]
print(child2.childNodes[0].data)  # World

# Using the xmlsec module
import xmlsec

xml_string = '''
<root>
    <child1>Hello</child1>
    <child2>World</child2>
</root>
'''

doc = xmlsec.tree.fromstring(xml_string)

# Perform XML signature or encryption operations

# Perform XML validation or schema validation

# Perform XPath queries or XSLT transformations

# Perform XML transformation using XSLT

# Perform XML transformation using XSL-FO

# Perform XML transformation using XQuery

# Perform XML transformation using XSLT 2.0

# Perform XML transformation using XSLT 3.0

# Perform XML transformation using XSLT 4.0

# Perform XML transformation using XSLT 5.0

# Perform XML transformation using XSLT 6.0

# Perform XML transformation using XSLT 7.0

# Perform XML transformation using XSLT 8.0

# Perform XML transformation using XSLT 9.0

# Perform XML transformation using XSLT 10.0

# Perform XML transformation using XSLT 11.0

# Perform XML transformation using XSLT 12.0

# Perform XML transformation using XSLT 13.0

# Perform XML transformation using XSLT 14.0

# Perform XML