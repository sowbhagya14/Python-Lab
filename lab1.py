Python 3.7.3 (default, Aug 20 2019, 17:04:43) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[1,2,3,4,5,6,7,8]
>>> print(L)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> L.append(5)
>>> print(L)
[1, 2, 3, 4, 5, 6, 7, 8, 5]
>>> L.remove(2)
>>> print(L)
[1, 3, 4, 5, 6, 7, 8, 5]
>>> L.remove(8)
>>> print(L)
[1, 3, 4, 5, 6, 7, 5]
>>>print(L)
[1, 3, 4, 5, 6, 7, 8, 9, 10, 53]
>>> print(len(L))
10
>>>print(L.insert(2,1))
None
>>> print(L)
[1, 1, 1, 3, 1, 4, 5, 6, 7, 9, 10]
>>> del L[0]
>>> print(L)
[1, 1, 3, 1, 4, 5, 6, 7, 9, 10]
>>> print(L)
[1, 3, 4, 5, 6, 7, 8, 9, 10, 53]
>>> print(L.pop())
53
>>> print(L.pop(6))
8
>>> print(L)
[1, 3, 4, 5, 6, 7, 9, 10]


