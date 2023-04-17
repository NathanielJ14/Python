#1

x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30



#2
def iterateDictionary(some_list):
    print(some_list)

people = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(people)


#3
def iterateDictionary2(key_name, some_list):
    for i in range(0, len(people)):
        print(some_list[i][key_name])
    return some_list[i][key_name]

iterateDictionary2("first_name", people)
print(iterateDictionary2)


#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    locations = len(some_dict["locations"])
    print( str(locations) + " LOCATIONS")
    for i in range(0, len(some_dict["locations"])):
        print(some_dict["locations"][i])
    instructors = len(some_dict["instructors"])
    print( str(instructors) + " INSTRUCTORS")
    for i in range(0, len(some_dict["instructors"])):
        print(some_dict["instructors"][i])
    return printInfo

printInfo(dojo)
