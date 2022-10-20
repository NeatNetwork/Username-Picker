adjectives = ['sassy', 'sad', 'jumpy', 'quiet', 'sleepy', 'noisy', 'neat', 'messy', 'organised', 'thinking', 'working', 'trying', 'typing', 'typed', 'done', 'thought', 'motorised', 'energised', 'troubled']
objects = ['porpoise', 'tutle', 'frog', 'goat', 'leamur', 'telly', 'table', 'helmet', 'computer', 'basket', 'tree', 'grass', 'flower', 'pot', 'plate', 'fork', 'beef', 'pork', 'chicken']
import random
first = random.choice(adjectives)
second = random.choice(objects)
third = random.choice(range(100, 999))
a = input("Welcome to Neat's Username Generator")
print("your username is " + str(first) + str(second) + str(third))
sleep(2)


