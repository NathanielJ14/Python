#countdown
my_list = []
def count_down(num):
    for i in range(num, -1, -1):
        my_list.append(i)

count_down(5)
print(my_list)

#print and return
print_list = [5,8]
def print_return():
    print(print_list[0])
    return(print_list[1])

print_return()


#first plus length
plus_list = [10,3,4,6,1]

def first_plus_length():
    sum  = plus_list[0] + len(plus_list)
    print(sum)

first_plus_length()

# value greater than second
old_list = [2,4,7,2,5,8]

def values_greater(list):
    second_num = list[1]
    for i in range(0, len(list)):
        if list[i] > second_num:
            print(list[i])

values_greater(old_list)


# this length that value
def length_and_value(size, value):
    print(str(value) * size)

length_and_value(5,8)