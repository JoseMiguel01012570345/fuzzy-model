import bisect
my_list = [('apple', 3), ('banana', 2), ('cherry', 1), ('date', 4)]

# Sort the list of tuples based on the second element of each tuple
sorted_list = sorted(my_list, key=lambda x: x[1])
index = bisect.bisect_left(sorted_list, ('dat', 3))

if index != len(my_list) and my_list[index] == ('dat', 3):
    
    print("item found")
