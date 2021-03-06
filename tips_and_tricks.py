#!/usr/bin/env python
# -*- coding: utf-8 -*-

# enumerate, to get index & item in the mean time
ss = ('pitt', 'patt', 'matt')
for i, s in enumerate(ss):
    print(i, s)


# input validation using sets
vv = {'patt', 'matt', 'pitt', 'dan', 'din', 'don'}
iv = {'patt', 'matt', 'pitt', 'rick'}

print(iv.intersection(vv))
print(iv.difference(vv))
print(iv.issubset(vv))

# for else
for v in vv:
    if v.startswith('a'):
        break
else:
    # if we don't reach the break, do this
    print('never reached the break stmt')

# conditional expressions
g = 4
n = g if g%3 else g-1
m = None
m = g if m is not None else 'gest'
print('Hello, %s'%m)

# more complex list comprehension
n = [i for i in range(10)]
s = [x for x in n if x%2]
t = [y if y%2 else y*2 for y in n]

# generators
# use them when you only need to loop
# over the object once
n = [i for i in range(10)]
s = (x for x in n if x%2)
k = next(s)
print(k)

# dictionary comprehension
teachers = {
 'Andy': 'English',
 'Joan': 'Maths',
 'Alice': 'Computer Science'
    }

subjects = {s: t for t, s in teachers.items()}
print(subjects)

# zip
n = ('a', 'b', 'c', 'd', 'e')
z = range(5)
for i,j in zip(n, z):
    print(i,j)

y = dict(zip(n,z))
print(y)

# itertools
from itertools import accumulate, chain, compress, dropwhile
# x is an iterator
print('accumulate')
x = accumulate([1,2,3,4,5])
print(next(x))
print(next(x))

# x is an iterator
# takes * iterables and yield values
# as if one iterable given
print('chain')
x= chain([1,2,3], [9,8,7])
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print('compress')
data = [1,2,3,4,5,6,7,8,9]
selector = [x%2 for x in data]
z = compress(data, selector)
#print(next(z))
# list can take an iterator as argument
print(list(z))

print('dropwhile')
mm = dropwhile(lambda y: y != 5, data)
print(list(mm))

# collections module
print('defaultdict')
from collections import defaultdict
order = (
    ('Mark', 'Steak'),
    ('Andrew', 'Veggie Burger'),
    ('James', 'Steak'),
    ('Mark', 'Beer'),
    ('Andrew', 'Beer'),
    ('James', 'Wine'),
    )

group_order = defaultdict(list)
for name, menu_item in order:
    group_order[name].append(menu_item)
print(group_order)

# decorators, again, and again

# always use wraps when writing a decorator
from functools import wraps

# our decorator
def power(func):
    # wraps the decorated function
    # to keep things like doc
    @wraps(func)
    def _pow(num):
        return func(num) ** 4
    return _pow

@power
def plus(num):
    """add 1 to a number"""
    return num + 1


# if we want to givean argument to our decorator
# we should write the decorator function inside another function
def power(pow):
    """power is a function that return the _power decorator"""
    def _power(func):
        @wraps(func)
        def _pow(num):
            return func(num) ** pow
        return _pow
    return _power

@power(7)
def plus(num):
    """add 1 to a number"""
    return num + 1


# a more useful decorator,
# with * and ** operators
import webbrowser

def cache(obj):
    saved = obj.saved = {}
    @wraps(obj)
    # our decorator can take any number & kind of arguments
    def memoizer(*args, **kwargs):
        # retrieve all the keys
        key = str(args) + str(kwargs)
        # if key not in cache, process with function
        if key not in saved: saved[key] = obj(*args, **kwargs)
        return saved[key]
    return memoizer

@cache
def web_lookup(url):
    page = webbrowser.open(url)
