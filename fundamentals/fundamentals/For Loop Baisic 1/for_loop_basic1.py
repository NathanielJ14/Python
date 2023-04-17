#print all integers from 0 to 150
for i in range(0, 151):
    print(i)

#print the multiples of 5 from 1,000
for i in range(5, 1001, 5):
    print(i)

#Counting the Dojo Way
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#Big Number
sum = 0
for i in range(0, 500001):
    sum += i
print(sum)

#Countdown by Fours
for i in range(2018, -1, -4):
    print(i)

    #Flexible Counters
lowNum = 2
highNum = 10
mult = 2
for i in range(lowNum, highNum, mult):
    print(i)