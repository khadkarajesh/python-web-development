# declare and initialize integer
a = 5

# declare and initialize float
b = 5.4

# declare and initialize boolean
result = True

# check type of variable
type(a)

# get help
# help('modules')
# help('str')
# help('bool')

# type conversion
a = str(a)
print(a)
print(type(a))

a = float(a)
print(a)
print(type(a))

# ---------- list ------------

# declare list
data = [4, 5, 6]

# declare list
data = list()

data.append(4)
data.remove(5)
data.insert(1, 3)

data.sort()

# pop element of index 0
data.pop(0)

# ---------- Dictionary -------------

user = dict()
# OR
user = {}

user['name'] = 'Bob'
user['address'] = 'USA'
user['profession'] = 'Engineer'

print(user)

user = {'name': 'Bob',
        'address': 'USA',
        'profession': 'Engineer'}

print(user.keys())
print(user.get('name'))
print(user.values())
print(user.items())

for key, value in user.items():
    print(F'{key} : {value}')


# nested dictionary

address = {
    'latitude': 1234,
    'longitude': 23456
}

# add address of user
user['address'] = address

# update latitude value to 500
user['address']['latitude'] = 500

# ------------ Tuple ----------
token = (1)

token = tuple(1, 'Jhon', 3.5)

print(type(token))

token = (1,)

print(type(token))

key, value = [2, 3]

# swap number
a = 5
b = 6
a, b = b, a
print(a, b)

# right side of tuple can be of any type string, list, tuple
name, domain = 'bob@google.com'.split('@')

# tuple comparision
if (5, 6, 7) > (1, 2, 4):
    print(True)

# access tuple's  element by index
values = (5, 6, 7)
print(values[1])

# ----------- set -------------

set_a = set()
set_b = set()

set_a.add(1)
set_a.add(2)

set_b.add(3)
set_b.add(4)

set_a.union(set_b)

# can perform all functions of set







