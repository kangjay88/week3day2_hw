#QUESTION 1:
# Filter out all of the empty strings from the list below
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
def a_places(place):
    if place == " " or place == "  " or place == "":    #there is probably a better way to do this.. \s?
        False
    else:
        return True

new_places = list(filter(a_places, places))
print(new_places)


#QUESTION 2:
#Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
lowercaselist = list(map(lambda name: name.lower(), author))
last_name = sorted(lowercaselist, key = lambda name: name.split()[-1])
print(last_name)  #wasn't sure how to capitalize after sorting..with title?


#QUESTION 3:
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
#`Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
new_places = str(places)
import re
pattern = re.compile('[0-9]+')
found = list(pattern.findall(new_places))

result = list(map(lambda num: (9/5)*int(num) + 32, found))
print(result)

#QUESTION 4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.
# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8

def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)

print(fib(5))
