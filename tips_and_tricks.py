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
