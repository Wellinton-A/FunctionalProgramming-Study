from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_my_pets(pets):
    return pets.upper()

print(list(map(capitalize_my_pets, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers[::-1])))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def scores_over_50(li):
    return li > 50

print(list(filter(scores_over_50, scores)))
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(lambda acc,item: acc+item, my_numbers + scores))

my_list = [5,4,3,9]
print(list(map(lambda item: item**2, my_list)))



a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key=lambda x: x[1])

print(a)


my_numb = [num for num in map(lambda item: item**2, range(100))]
my_numb2 = [num for num in filter(lambda item: item%2 == 0, my_numb)]
print(my_numb)
print(my_numb2)

my_numb3 = [num**2 for num in range(100)]
my_numb4 = [num**2 for num in range(100) if num %2 ==0]
print(my_numb3)
print(my_numb4)

my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list({lett for lett in some_list if some_list.count(lett) > 1})

print(duplicates)
