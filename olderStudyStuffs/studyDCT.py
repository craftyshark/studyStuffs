
dct = {}

# so we have a few things to do here
# wait lets be dumb and not break things down, all we need to do is do a for each
# and loop through a range, setting the key to i and the value to i*i

for i in range(1,20):
    dct[i] = i*i

print(dct)

#2

dict1 = {'a': 100, 'b': 200}

dict1['c'] = 300

#3

family = {
    "grandpa": {"dad": {"me": {}, "brother": {}}, "uncle": {"cousin": {}}}
}

family["grandpa"]["aunt"] = {"nephew": {}}

#4 I do not know what a dict comp is 

#5

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 200, 'd': 400}

# for d in dict1:
#     if d in dict2:
#         continue
#     else:
#         dict2[d] = dict1[d]

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 200, 'd': 400}

dict1.update(dict2)


print (dict1)

# I will set up a max and min int from the start
max = None
min = None

#we will ignore negatives for today

for d in dict1:
    if (max is None or max < dict1[d]):
        max = dict1[d]
    
    if (min is None or min > dict1[d]):
        min = dict1[d]

    print (d)

    print(min, max)