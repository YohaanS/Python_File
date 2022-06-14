# This is logging
import logging
from turtle import back
logger = logging.getLogger(__name__)
# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file_log_special.log")

# Code for the level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(leelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error("This is an error")
# This is a configuration file from logging
import logging.config

from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path)

logger = logging.getLogger('simpleExample')
logger.debug("This is a debug message")
# This code can make stuff make errors
class alueTooHighError(Exception):
    pass

class alueTooSmallError(Exception):
    def __init__(self, message, alue):
        self.message = message
        self.alue = alue


    
def test_alue(x):
    if x > 100:
        raise alueTooHighError("alue is too high!")
    if x < 5:
        raise alueTooSmallError("alue is too small!", x)

             
try:
   test_alue(1)
except alueTooHighError as e:
    print(e)    
except alueTooSmallError as e:
    print(e.message)
try:
    a = [1, 2, 3]
    al = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)
# These code are abot functions
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result




print(raise_to_power(2, 3))
# This is a game
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
question_prompts = [
    "What color are apples?\n(a) Red/green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
    "What color are blackberries?\n(a) black\n(b) Red\n(c) purple\n\n",
]


questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b"),
    Question(question_prompts[3],"a"),
    ]
   
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)
# This is about lists
list_org = ["banana", "cherry", "apple"]

list_cpy = list_org[:]


list_cpy.append("lemon")
print(list_cpy)
print(list_org)

mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]

print(mylist)
print(b)
# This is about json
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, separators=('; ', ' = '), sort_keys=True)
print(personJSON)
with open('person.json', "r") as file:
    person = json.load(file)
    print(person)
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

from json import JSONDecodeError, JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
           return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o) 
userJSON = UserEncoder().encode(user) 
print(userJSON)
# This is about random numbers
import random

a = random.random()
print(a)
import random

a = random.uniform(1, 10)
print(a)
import random

a = random.randint(1, 10)
print(a)
import random

a = random.randrange(1, 10)
print(a)
import random

a = random.randrange(1, 10)
print(a)
import random

a = random.normalvariate(0, 1)
print(a)
mylist = list("dda")
a = random.shuffle(mylist)
print(mylist)
import random

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))
# This is about secrets
import secrets

a = secrets.randbelow(10)
print(a)
import secrets

a = secrets.randbits(4)
# 1111
print(a)
import secrets

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)
#Numpy
import numpy as np

arr = np.random.rand(7, 3)
print(arr)
a = np.random.randint(0, 10, (3,4))
print(a)
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)
#This is about decorators
def start_end_decorator(func):
    
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper    

@start_end_decorator
def print_name():
    print("Alex")

print_name()
import functools
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper    

@start_end_decorator
def add5(x):
    return x + 5

print(add5.__name__)
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat             

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet('Alex')
import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper    

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello("Alex")
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)



@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()
def mygenerator():
    yield 1
    yield 2
    yield 3

mg = mygenerator()

print(sum(mg))

def mygenerator():
    yield 1
    yield 2
    yield 3

mg = mygenerator()

value = next(mg)
print(value)
value = next(mg)
print(value)
value = next(mg)
print(value)
def mygenerator():
    yield "3"
    yield "2"
    yield "9"

mg = mygenerator()

print(sorted(mg))
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1
    print("End")
cd = countdown(4)

value = next(cd)

print(value)


print(next(cd))
print(next(cd))
print(next(cd))