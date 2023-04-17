num1 = 42 #variable declaration Number
num2 = 2.3 #variable declaration Number
boolean = True #variable declaration Boolean
string = 'Hello World' #variable declaration String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Tuples
print(type(fruit)) #type check 
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #add value to a list
print(person['name']) #log statement
person['name'] = 'George' #change value John to George in person
person['eye_color'] = 'blue' #add value of eye_color to = blue
print(fruit[2]) #access value and print banana

if num1 > 45: #if  
    print("It's greater") #Log value
else: #else
    print("It's lower") #Log value

if len(string) < 5: #if 
    print("It's a short word!") #Log value
elif len(string) > 15: #else if 
    print("It's a long word!") #Log value
else: #else
    print("Just right!") #Log value

for x in range(5): #for loop start
    print(x) #log value
for x in range(2,5): 
    print(x)
for x in range(2,10,3):
    print(x) #end
x = 0 #variable declaration Number
while(x < 5): #while loop start
    print(x) #log value
    x += 1 #increment 1 to x then end

pizza_toppings.pop() #Delete last value 
pizza_toppings.pop(1) #delete value of index 1

print(person) # log person 
person.pop('eye_color') # delete eye_color from person
print(person) # log person

for topping in pizza_toppings: #for loop 
    if topping == 'Pepperoni': #if
        continue
    print('After 1st if statement') #log data
    if topping == 'Olives': #if
        break #break

def print_hello_ten_times(): #function parameter
    for num in range(10): #for
        print('Hello') #log data

print_hello_ten_times() 

def print_hello_x_times(x): #function parameter
    for num in range(x): #for
        print('Hello') 

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function parameter
    for num in range(x): #for
        print('Hello')

print_hello_x_or_ten_times() #log data
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)